from utils.search_index import SearchIndex


si = SearchIndex()

def test_should_return_empty():
  assert si.search("", 3) == []
  assert si.search("is your problems", 0) == []
  assert si.search("", 0) == []


def test_should_return_data():
  assert len(si.search("is your problems", 3)) == 3
  assert len(si.search("random text", 3)) == 0