import datetime
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Column, Integer, ForeignKey, String, PrimaryKeyConstraint, Enum, DateTime

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    jobTitle = Column(String)

    def save(self):
        db.session.add(self)
        db.session.commit()


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        include_relationships = True
        load_instance = True


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class Labor(db.Model):
    __tablename__ = 'labors'

    labor_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    houseNu = Column(Integer)
    farmName = Column(String)

    def labor_save(self):
        db.session.add(self)
        db.session.commit()


class LaborSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Labor
        include_relationships = True
        load_instance = True


labor_schema = LaborSchema()
labors_schema = LaborSchema(many=True)


class Form(db.Model):
    __tablename__ = 'form'
    form_id = Column(Integer, primary_key=True)
    template_id = Column(Integer, ForeignKey('template.template_id'))
    filled_by = Column(Integer, ForeignKey('users.user_id'))
    farm_name = Column(String)
    barn_number = Column(Integer)
    cycle_number = Column(String)
    metadata_id = Column(Integer, ForeignKey('metadata.metadata_id'))

    def save(self):
        db.session.add(self)
        db.session.commit()


class FormSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Form
        include_relationships = True
        load_instance = True


form_schema = FormSchema()
forms_schema = FormSchema(many=True)


class FormColumns(db.Model):
    __tablename__ = 'form_columns'
    form_id = Column(Integer, ForeignKey('form.form_id'), primary_key=True)
    column_title = Column(String, primary_key=True)


class FormColumnsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = FormColumns
        include_relationships = True
        load_instance = True


form__column_schema = FormColumnsSchema()
form_columns_schema = FormColumnsSchema(many=True)


class Metadata(db.Model):
    __tablename__ = 'metadata'
    metadata_id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    time = Column(String)
    title = Column(String)

    def __init__(self, date, time, title):
        self.date = date
        self.time = time
        self.title = title

    def save(self):
        db.session.add(self)
        db.session.commit()


class MetadataSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Metadata
        include_relationships = True
        load_instance = True


Metadata_Schema = MetadataSchema()
Metadatas_Schema = MetadataSchema(many=True)


class Template(db.Model):
    __tablename__ = 'template'
    template_id = Column(Integer, primary_key=True)
    type = Column(String)

    def __init__(self, template_name):
        self.template_name = template_name

    def save(self):
        db.session.add(self)
        db.session.commit()


class TemplateSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Template
        include_relationships = True
        load_instance = True


template_schema = TemplateSchema()
templates_schema = TemplateSchema(many=True)


class TemplateRow(db.Model):
    __tablename__ = 'template_row'
    template_id = Column(Integer, ForeignKey('template.template_id'), primary_key=True)
    row_title = Column(String, primary_key=True)
    __table_args__ = (PrimaryKeyConstraint(template_id, row_title),)

    def __init__(self, template_id, row_name):
        self.template_id = template_id
        self.row_name = row_name

    def save(self):
        db.session.add(self)
        db.session.commit()


class TemplateRowSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TemplateRow
        include_relationships = True
        load_instance = True


template_rows_schema = TemplateRowSchema()
template_rowss_schema = TemplateRowSchema(many=True)


class SubmittedData(db.Model):
    __tablename__ = 'submitted_data'
    template_id = Column(Integer, ForeignKey("template_row.template_id"), primary_key=True)
    row_title = Column(String, ForeignKey("template_row.row_title"), primary_key=True)
    form_id = Column(Integer, ForeignKey("form_columns.form_id"), primary_key=True)
    column_title = Column(String, ForeignKey("form_columns.column_title"), primary_key=True)
    data = Column(String)
    __table_args__ = (PrimaryKeyConstraint('template_id', 'row_title', 'form_id', 'column_title'),)


class SubmittedDataSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SubmittedData
        include_relationships = True
        load_instance = True


submitted_data_schema = SubmittedDataSchema()
submitted_datas_schema = SubmittedDataSchema(many=True)

with app.app_context():
    db.create_all()
