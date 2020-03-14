release: npm run --prefix static sass
web: bin/start-nginx gunicorn -b unix:///tmp/rpscene.socket rpscene.wsgi
