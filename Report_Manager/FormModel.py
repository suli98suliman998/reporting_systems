from flask import render_template

from Report_Manager.TemplateModel import get_row_titles_by_template_id
from model import FormColumns, db, Form, form_schema


def get_form_columns_by_form_id(form_id):
    form_columns = db.session.query(FormColumns.column_title) \
        .filter(FormColumns.form_id == form_id) \
        .all()
    return [column[0] for column in form_columns]


def get_form_by_id(form_id: int):
    form = Form.query.filter_by(form_id=form_id).first()
    f = Form(form_id=form.form_id, template_id=form.template_id, filled_by=form.filled_by, farm_name=form.farm_name, barn_number=form.barn_number, cycle_number=form.cycle_number, metadata_id=form.metadata_id)
    return f

