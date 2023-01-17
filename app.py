from flask import request, jsonify, render_template

from Report_Manager.FormModel import get_form_columns_by_form_id
from Report_Manager.TemplateModel import get_row_titles_by_template_id
from model import app, TemplateRow, db


@app.route('/template/<int:template_id>/rows')
def get_template_rows(template_id):
    row_titles = get_row_titles_by_template_id(template_id)

    return jsonify(row_titles)


@app.route('/form/<int:form_id>')
def build_form(form_id):
    column_names = get_form_columns_by_form_id(form_id)
    row_names = get_row_titles_by_template_id(form_id)
    return render_template('form_builder.html', column_names=column_names, row_names=row_names)


if __name__ == '__main__':
    app.run(debug=True)
