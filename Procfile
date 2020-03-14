web: python manage.py makemigrations --no-input && python manage.py migrate --no-input && echo ${NGINX_BASIC_AUTH} > .htpasswd && bin/start-nginx gunicorn -b unix:///tmp/rpscene.socket rpscene.wsgi
