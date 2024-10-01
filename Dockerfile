FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD python manage.py makemigrations && python manage.py migrate && gunicorn --bind 0.0.0.0:80 --workers 3 tracking_api.wsgi:application