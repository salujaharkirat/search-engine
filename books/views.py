from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404, JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from django.core.cache import cache
import requests
# Create your views here.
import json

from utils.search_index import SearchIndex


AUTHOR_API_END_POINT = "https://ie4djxzt8j.execute-api.eu-west-1.amazonaws.com/coding"
HEADERS = {"Content-Type": "application/json"}


@csrf_exempt
@api_view(["POST"])
def get_books(request):
  load_data = json.loads(request.body)
  queries = load_data.get("queries")
  k = load_data.get("k")

  if not queries or not len(queries):
    raise ValidationError("Please pass list of queries...")

  if not isinstance(queries, list):
    queries = [queries]

  if not k:
    raise ValidationError("Please pass number of results required...")

  si = SearchIndex()
  result = []
  author_map = {}
  for query in queries:
    relevant_search = si.search(query, k)
    for datum in relevant_search:
      author_map[datum['id']] = None
    result.append(relevant_search)

  for key in author_map.keys():
    payload = json.dumps({
      "book_id": int(key)
    })

    cache_data = cache.get(key)
    if cache_data:
      data = cache_data
    else:
      data = requests.post(url = AUTHOR_API_END_POINT, data=payload, headers=HEADERS).json()
      cache.set(key, data)
    author_map[key] = data['author']

  for row in result:
    for datum in row:
      datum['author'] = author_map[(datum['id'])]

  return JsonResponse({"books": result}, safe=False)


