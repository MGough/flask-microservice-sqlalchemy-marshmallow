from flask import Blueprint, jsonify

blueprint = Blueprint("health", __name__, url_prefix="/health")


@blueprint.route("/", methods=["GET"])
def healthcheck():
    # TODO: Update this to also report on its own dependencies
    # TODO: See https://github.com/MGough/flask-microservice-sqlalchemy-marshmallow/issues/3
    return jsonify(healthy=True), 200
