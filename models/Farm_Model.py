from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farm_name = db.Column(db.String, nullable=False)
    houses_count = db.Column(db.Number, nullable=False)

    def __init__(self, farm_name, houses_count):
        self.farm_name = farm_name
        self.houses_count = houses_count


class FarmSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Farm
        include_relationships = True
        load_instance = True


farm_schema = FarmSchema()
farms_schema = FarmSchema(many=True)


def db_add_farm(farm_name, houses_count):
    new_farm = Farm(farm_name=farm_name, houses_count=houses_count)
    db.session.add(new_farm)
    db.session.commit()


def db_delete_farm(farm_id):
    farm = Farm.query.get(farm_id)
    db.session.delete(farm)
    db.session.commit()


def db_edit_farm(farm_id, farm_name=None, houses_count=None):
    farm = Farm.query.get(farm_id)
    if farm_name:
        farm.time_from = farm_name
    if houses_count:
        farm.time_to = houses_count
    db.session.commit()


def db_get_farm_by_id(farm_id):
    return Farm.query.get(farm_id)


def db_get_farm_by_name(farm_name):
    return Farm.query.filter_by(farm_name=farm_name).first()


def db_get_all_farms():
    return Farm.query.all()
