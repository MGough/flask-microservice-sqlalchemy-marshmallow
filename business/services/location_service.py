from flask import Blueprint, request, jsonify

from business.models.location import Location, database, LocationSchema

blueprint = Blueprint('location', __name__, url_prefix='/location')
location_schema = LocationSchema()


@blueprint.route("/", methods=["POST"])
def create_location():
    location = location_schema.load(request.json)
    database.session.add(location)
    database.session.commit()

    return jsonify(id=location.id), 200


@blueprint.route("/<int:location_id>", methods=["GET"])
def get_location(location_id):
    location = Location.query.get(location_id)
    return location_schema.dump(location), 200
