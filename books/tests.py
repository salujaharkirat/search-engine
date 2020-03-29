
from .views import get_books
from rest_framework import status
from rest_framework.test import APITestCase

import json

class TestCalls(APITestCase):
  def test_empty_query_list(self):
    data = {
      "queries": [],
      "k": 3
    }

    url = '/api/v0/books/'
    response = self.client.post(url, data, format='json')
    content = json.loads(response.content)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


  def test_empty_query(self):
    data = {
      "queries": "",
      "k": 3
    }

    url = '/api/v0/books/'
    response = self.client.post(url, data, format='json')
    content = json.loads(response.content)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_empty_k(self):
    data = {
      "queries": "",
      "k": 0
    }

    url = '/api/v0/books/'
    response = self.client.post(url, data, format='json')
    content = json.loads(response.content)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_get_books_data(self):
    data = {
      "queries": ["is your problems"],
      "k": 3
    }

    url = '/api/v0/books/'
    response = self.client.post(url, data, format='json')
    content = json.loads(response.content)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(content['books'][0]), 3)