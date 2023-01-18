from flask import jsonify, render_template, request

from Report_Manager.FormModel import get_form_columns_by_form_id
from Report_Manager.TemplateModel import get_row_titles_by_template_id
from User import UserModel

from model import app, db, Users, Labor


@app.route('/template/<int:template_id>/rows')
def get_template_rows(template_id):
    row_titles = get_row_titles_by_template_id(template_id)

    return jsonify(row_titles)


@app.route('/form/<int:form_id>')
def build_form(form_id):
    column_names = get_form_columns_by_form_id(form_id)
    row_names = get_row_titles_by_template_id(form_id)
    return render_template('form_builder.html', column_names=column_names, row_names=row_names)


@app.route('/labor_form')
def view_labor_form():
    return build_form(1)


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/register_user', methods=['GET', 'POST'])
def view_user_registration():
    from User.UserController import controller_create_user
    return controller_create_user()


@app.route('/register_labor', methods=['GET', 'POST'])
def view_labor_registration():
    from User.UserController import controller_create_labor
    return controller_create_labor()


if __name__ == '__main__':
    app.run(debug=True)
