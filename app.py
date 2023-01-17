from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = '\x8afmI\xc5\x17Rh\x11\xd96Z\xa0\xf1\xfdm\xc0\xfc/\xce\xb4\x9d\xed/'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


with app.app_context():
    db.create_all()
