#!/bin/sh

sleep 10

python manage.py migrate
python manage.py createcachetable
python manage.py collectstatic  --noinput
docker-compose run web python manage.py loaddata fixtures.json
gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000

exec "$@"