from flask import jsonify, render_template

from Report_Manager.TemplateModel import get_row_titles_by_template_id
from model import app


@app.route('/labor_form/<shift>', methods=['GET', 'POST'])
def view_labor_form(shift):
    rows = get_row_titles_by_template_id(1)
    print(rows)
    print([shift])
    return render_template('form_builder.html', column_names=[shift], row_names=rows)


@app.route('/form/<type>', methods=['GET', 'POST'])
def view_form(type):
    from Report_Manager.Reporting_services import get_form
    return get_form(type)


@app.route('/labor_pre_form', methods=['GET', 'POST'])
def view_labor_pre_form():
    from Report_Manager.FormController import controller_daily_barn_pre_form
    return controller_daily_barn_pre_form()


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
