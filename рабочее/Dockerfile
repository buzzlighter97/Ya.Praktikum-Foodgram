FROM python:3.8.5

WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
RUN sh entrypoint.sh
RUN chmod ugo+x entrypoint.sh
CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000
