from business.application_factory import database, marshmallow


class Location(database.Model):
    __tablename__ = "location"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String, nullable=False)


class LocationSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Location
        load_instance = True
        sqla_session = database.session
