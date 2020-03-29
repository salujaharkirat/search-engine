# search-engine


## Steps
  1. virtual venv
  2. source venv/bin/activate
  3. pip install -r requirements.txt
  4. python manage.py migrate
  5. python -m utils.prepare_mock
  6. python manage.py runserver


## Points to note

  1. Please make sure that the redis server is running on port 6379
  2. Please run prepare `prepare_mock` inside utils folder to set up pre-processing environment


## Logic

  1. I have used hashed table for pre-processing the summary information
  2. When we run `prepare_mock` inside utils it creates an index based hash table with words as key and value as an object with key as summary id and value as number of occurrences in that summary.
    For example, consider a following simple index based hash:-

      ```
        {
          "problem": {
            "1": 1,
            "48": 2
          }
        }
      ```
  3. Also the `prepare_mock` creates a summary object with summary id as key. This is done mainly for fast retrievals while adding author to the summary.

  4. Since multiple summaries can have similar books, querying for book author for each summary is not really a scalable approach. So to handle the same I iterate over the result and make an object with summary id as object. Next, I iterate over this and make api call for book author saving the same in the object values. Once this is established, I iterate over the nested list and get author based on summary id from above map. Adding to this, I have used redis cache to save author data, as it is not going to change in future. This increases the performance drastically.


  5. In my algorithm, the space complexity is a bit on the upper side, but I feel that for gaining speed we need to make a tradeoff somewhere.


  6. This logic will not work now for substrings, for which we need to add fuzzy logic it. It can be implemented by using something like `fuzzy-wuzzy` package.
