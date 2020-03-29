from collections import defaultdict

import json

def parse_data():
  data = {}
  with open('utils/data.json', 'r') as f:
    data = json.loads(f.read())

  indexed_dict = defaultdict()
  summary = defaultdict()

  summaries = data['summaries']

  for data in summaries:
    id = str(data['id'])
    summary[id] = data['summary']
    for word in data['summary'].split():
      if word in indexed_dict:
        if id in indexed_dict[word]:
          indexed_dict[word][id] += 1
        else:
          indexed_dict[word][id] = 1
      else:
        indexed_dict[word] = {}
        indexed_dict[word][id] = 0

  f = open('utils/indexed_summaries.json', "a")
  f.write(json.dumps(indexed_dict))
  f.close()

  f = open('utils/summary_dict.json', "a")
  f.write(json.dumps(summary))
  f.close()


parse_data()

