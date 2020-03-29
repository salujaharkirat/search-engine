from collections import defaultdict
import json

class SearchIndex:
  def __init__(self):
    self._index = defaultdict()
    self._summary = defaultdict()
    self._titles = []

    with open('utils/indexed_summaries.json', 'r') as f:
      self._index =  json.loads(f.read())

    with open('utils/summary_dict.json', 'r') as f:
      self._summary =  json.loads(f.read())

    with open('utils/data.json', 'r') as f:
      self._titles = json.loads(f.read())['titles']

  def get_relevant_data(self, query_map, k):
    temp_result_map = defaultdict(int)

    for key, value in query_map.items():
      try:
        key_data = self._index[key]
      except:
        key_data = {}

    # Searching for words inside the indexed dictionary and incrementing the count
      for key,value in key_data.items():
        if key in temp_result_map:
          temp_result_map[key] += value
        else:
          temp_result_map[key] = value

    # Reverse sorted the dictionary with max count
    sorted_temp_reverse_map = sorted(temp_result_map.items(), key=lambda kv: kv[1], reverse=True)

    result = list(sorted_temp_reverse_map)[:k]

    final_result = []

    for element in result:
      id = element[0]
      final_result.append({
        "id": id,
        "summary": self._summary[id],
        "title": self._titles[int(id)]
      })

    return final_result

  def search(self, query, k):
    if not query or not len(query):
      return []

    if k == 0:
      return []

    query_map = {}

    # Splitting strings based on words and getting count of each word
    for datum in query.split():
      if datum in query_map:
        query_map[datum] += 1

      else:
        query_map[datum] = 1

    return self.get_relevant_data(query_map, k)


