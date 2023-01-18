from flask import render_template

from Report_Manager.TemplateModel import get_row_titles_by_template_id
from model import FormColumns, db


def get_form_columns_by_form_id(form_id):
    form_columns = db.session.query(FormColumns.column_title) \
        .filter(FormColumns.form_id == form_id) \
        .all()
    return [column[0] for column in form_columns]


def build_form(form_id):
    column_names = get_form_columns_by_form_id(form_id)
    row_names = get_row_titles_by_template_id(form_id)
    return render_template('form_builder.html', column_names=column_names, row_names=row_names)