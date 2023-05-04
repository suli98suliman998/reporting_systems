import datetime
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Column, Integer, ForeignKey, String, PrimaryKeyConstraint, Enum, DateTime

basedir = 'reporting_systems'

app = Flask(__name__)
app.secret_key = 'IM_THE_BEST'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + '../database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    password = Column(String)
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

    def save(self):
        db.session.add(self)
        db.session.commit()


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
    order = Column(Integer)
    __table_args__ = (PrimaryKeyConstraint(template_id, row_title),)

    def __init__(self, template_id, row_name, order):
        self.template_id = template_id
        self.row_name = row_name
        self.order = order

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_template_id_by_type(template_type):
        template = Template.query.filter_by(template_type=template_type).first()
        if template:
            return template.template_id
        else:
            return None


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

    def __init__(self, template_id, row_title, form_id, column_title, data):
        self.template_id = template_id
        self.row_title = row_title
        self.form_id = form_id
        self.column_title = column_title
        self.data = data

    def save(self):
        db.session.add(self)
        db.session.commit()


class SubmittedDataSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SubmittedData
        include_relationships = True
        load_instance = True


submitted_data_schema = SubmittedDataSchema()
submitted_datas_schema = SubmittedDataSchema(many=True)


class Farm(db.Model):
    __tablename__ = 'farm'
    farm_id = Column(Integer, primary_key=True)
    farm_name = Column(String)
    total_barn_count = Column(Integer)
    area = Column(String)

    def __init__(self, farm_name, total_barn_count, area):
        self.farm_name = farm_name
        self.total_barn_count = total_barn_count
        self.area = area

    def save(self):
        db.session.add(self)
        db.session.commit()


class FarmSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Farm
        include_relationships = True
        load_instance = True


famr_schema = FarmSchema()
farms_schema = FarmSchema(many=True)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(120), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()


class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        include_relationships = True
        load_instance = True


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(120), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()


class TypeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Type
        include_relationships = True
        load_instance = True


type_schema = TypeSchema()
types_schema = TypeSchema(many=True)


class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String(120), nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()


class SupplierSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Supplier
        include_relationships = True
        load_instance = True


Supplier_schema = SupplierSchema()
Suppliers_schema = SupplierSchema(many=True)

with app.app_context():
    db.create_all()
