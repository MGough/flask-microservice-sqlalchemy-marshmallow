# flask-microservice-sqlalchemy-marshmallow
Quite a mouthful. This is a starter project for a flask microservice.
It uses SQLAlchemy to interact with a database, and Marshmallow for
serialization of objects.

The flask app itself is written using the application factory pattern,
to allow simple integration with WSGI servers such as Gunicorn.

## Application Configuration
Dynaconf has been used for simple configuration, a `settings.yml` file
is provided for development purposes and to help document the
configurable values. However dynaconf allows us to set these values as
environment variables instead which is usually preferable (see
[The 12 Factor app](https://12factor.net))

Flask config values can be set here, as well as our own custom
configuration values. See the [dynaconf documentation](https://dynaconf.readthedocs.io/en/latest/)

## Setting up your environment
As per the Dockerfile, this project is using Python 3.8 (disclaimer: this will inevitably fall out of date,
double check the dockerfile) so you'll need a Python 3.8 environment.

To ensure code quality is maintained, and to ensure your PR pipeline passes you will need to set up pre-commit.
```shell script
pip install -r requirements-dev.txt
```

The first time you do this you'll also need to run: `pre-commit install`. This will set up the autoformatting hooks.

For running the application locally (i.e. not in a docker container) you'll need to run `pip install -r requirements.txt`

## Running for development (debugging)
`development_wsgi.py` is provided to simplify running of the application.
`flask run` with the appropriate arguments could also be used, but the
`development_wsgi` file makes it simple to start the debugger in PyCharm
community edition, which I why I've included it.

## Running tests

### Unit tests
Assuming your development environment is set up, it's as simple as running `tox`.

### Integration tests
To run the integration tests you'll need docker installed & running, as well as
a working internet connection (to pull docker images).

You'll then need to run `tox -e integration`
