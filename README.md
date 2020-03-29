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

