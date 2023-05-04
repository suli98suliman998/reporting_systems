from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class time_frames(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_from = db.Column(db.Integer, nullable=False)
    time_to = db.Column(db.Integer, nullable=False)

    def __init__(self, time_from, time_to):
        self.time_from = time_from
        self.time_to = time_to


class TimeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = time_frames
        include_relationships = True
        load_instance = True


farm_schema = TimeSchema()
farms_schema = TimeSchema(many=True)


def db_add_farm(time_from, time_to):
    new_farm = time_frames(time_from=time_from, time_to=time_to)
    db.session.add(new_farm)
    db.session.commit()


def db_delete_farm(time_id):
    time = time_frames.query.get(time_id)
    db.session.delete(time)
    db.session.commit()


def db_edit_farm(time_frames_id, time_from=None, time_to=None):
    time = time_frames.query.get(time_frames_id)
    if time_from:
        time.time_from = time_from
    if time_to:
        time.time_to = time_to
    db.session.commit()


def db_get_all_times():
    return time_frames.query.all()
