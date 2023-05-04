from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    user_type = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, nullable=True)

    def __init__(self, username, password, user_type, status):
        self.username = username
        self.password = password
        self.user_type = user_type
        self.status = status


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True



user_schema = UserSchema()
users_schema = UserSchema(many=True)


def db_add_user(username, password, user_type):
    new_user = User(username=username, password=password, user_type=user_type, status=True)
    db.session.add(new_user)
    db.session.commit()


def db_delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()


def db_edit_user(user_id, username=None, password=None, user_type=None):
    user = User.query.get(user_id)
    if username:
        user.farm_id = username
    if password:
        user.mortality_count = password
    if user_type:
        user.consumed_feed = user_type
    db.session.commit()


def db_get_user_by_id(user_id):
    return User.query.get(user_id)


def db_get_user_by_username(username):
    return User.query.filter_by(username=username).first()
