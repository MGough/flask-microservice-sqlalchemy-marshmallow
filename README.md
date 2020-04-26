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

## Running for development (debugging)
`development_wsgi.py` is provided to simplify running of the application.
`flask run` with the appropriate arguments could also be used, but the
`development_wsgi` file makes it simple to start the debugger in PyCharm
community edition, which I why I've included it.

