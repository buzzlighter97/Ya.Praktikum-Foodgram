#!/bin/sh

sleep 10

sudo python manage.py migrate
sudo python manage.py createcachetable
sudo python manage.py collectstatic  --noinput
sudo docker-compose run web python manage.py loaddata fixtures.json
sudo gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000

exec "$@"