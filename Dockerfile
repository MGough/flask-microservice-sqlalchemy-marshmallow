FROM python:3.8

RUN mkdir /app
WORKDIR /app

# By doing this separately to copying over our code we are able to cache our dependencies.
# This means that if a subsequent build only changes our code, and not requirements.txt,
# then we don't need to do a fresh install of all of our dependencies listed in requirements.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY business business
COPY config config

CMD gunicorn "business.application_factory:create_app()"