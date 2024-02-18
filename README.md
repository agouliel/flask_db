## Basic usage
`pip install -r requirements.txt`   
`flask --app flask_db run --host 0.0.0.0 --port 5001`   

## Test the main API endpoint
[http://localhost:5001/flask/api/songs](http://localhost:5001/flask/api/songs)

## Production
`pip install gunicorn`   
`.venv/bin/gunicorn flask_db:app -b :5001 --daemon`