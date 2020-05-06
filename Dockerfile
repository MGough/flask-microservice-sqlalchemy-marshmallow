FROM python:3.8

# By doing this separately to copying over our code we are able to cache our dependencies.
# This means that if a subsequent build only changes our code, and not requirements.txt,
# then we don't need to do a fresh install of all of our dependencies listed in requirements.txt
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt  --no-cache-dir

RUN useradd --create-home serviceuser
WORKDIR /home/serviceuser
USER serviceuser

COPY business business
COPY config config

CMD gunicorn --worker-tmp-dir /dev/shm -b 0.0.0.0:8000 "business.application_factory:create_app()"
