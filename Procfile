release: python manage.py makemigrations && python manage.py migrate
web: bin/start-nginx gunicorn -b unix:///tmp/rpscene.socket rpscene.wsgi
