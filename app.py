from flask import jsonify, render_template

from User import UserController
from Report_Manager.FormModel import get_form_columns_by_form_id
from Report_Manager.TemplateModel import get_row_titles_by_template_id
from User.UserController import controller_create_user
from model import app


@app.route('/template/<int:template_id>/rows')
def get_template_rows(template_id):
    row_titles = get_row_titles_by_template_id(template_id)

    return jsonify(row_titles)


@app.route('/form/<int:form_id>')
def build_form(form_id):
    column_names = get_form_columns_by_form_id(form_id)
    row_names = get_row_titles_by_template_id(form_id)
    return render_template('form_builder.html', column_names=column_names, row_names=row_names)


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def view_registration():
    return controller_create_user()


if __name__ == '__main__':
    app.run(debug=True)
