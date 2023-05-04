from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from Farm_Model import db_get_farm_by_name

db = SQLAlchemy()


class house_logs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.String, db.ForeignKey('Farm.id'))
    mortality_count = db.Column(db.Integer, nullable=False)
    consumed_feed = db.Column(db.Float, nullable=False)
    consumed_water = db.Column(db.Float, nullable=True)
    ph_level = db.Column(db.Float, nullable=True)
    temperature = db.Column(db.Float, nullable=True)
    avg_weight = db.Column(db.Float, nullable=True)
    lights_off_time = db.Column(db.Float, nullable=True)
    cycle_number = db.Column(db.Integer, nullable=True)

    def __init__(self, farm_name, mortality_count, consumed_feed, consumed_water, ph_level, temperature, avg_weight,
                 lights_off_time, cycle_number):
        self.farm_id = db_get_farm_by_name(farm_name)
        self.mortality_count = mortality_count
        self.consumed_feed = consumed_feed
        self.consumed_water = consumed_water
        self.ph_level = ph_level
        self.temperature = temperature
        self.avg_weight = avg_weight
        self.lights_off_time = lights_off_time
        self.cycle_number = cycle_number


class HouseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = house_logs
        include_relationships = True
        load_instance = True


#
house_schema = HouseSchema()
houses_schema = HouseSchema(many=True)


def db_add_house(farm_name, mortality_count, consumed_feed, consumed_water, ph_level, temperature, avg_weight,
                 lights_off_time, cycle_number):
    new_house = house_logs(farm_name=farm_name, mortality_count=mortality_count, consumed_feed=consumed_feed,
                           consumed_water=consumed_water, ph_level=ph_level, temperature=temperature, avg_weight=avg_weight,
                           lights_off_time=lights_off_time, cycle_number=cycle_number)
    db.session.add(new_house)
    db.session.commit()


def db_get_user_by_id(user_id):
    return house_logs.query.get(user_id)


def db_get_user_by_username(username):
    return house_logs.query.filter_by(username=username).first()

db_add_house("ss", 1, 1, 1, 1, 1, 1, 1, 1)