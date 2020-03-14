web: echo ${NGINX_BASIC_AUTH} > .htpasswd && bin/start-nginx gunicorn -b unix:///tmp/rpscene.socket rpscene.wsgi
