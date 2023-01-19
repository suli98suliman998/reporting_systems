from flask import jsonify, render_template, request

from Report_Manager.Reporting_services import submit_form, get_form
from Report_Manager.TemplateModel import get_row_titles_by_template_id
from model import app


@app.route('/labor_form/<shift>', methods=['GET', 'POST'])
def view_labor_form(shift):
    rows = get_row_titles_by_template_id(1)
    print(rows)
    print([shift])
    return render_template('form_builder.html', column_names=[shift], row_names=rows)


@app.route('/labor_pre_form', methods=['GET', 'POST'])
def view_labor_pre_form():
    if request.method == 'POST':
        cycle_number = request.form.get("cycle_number")
        shift = request.form.get("shift")
        columns = [shift]
        return get_form("Daily_Barn", cycle_number, columns)
    from Report_Manager.FormModel import get_form_columns_by_form_id
    shifts = get_form_columns_by_form_id(1)  # from form_coolumns

    return render_template('daily_barn_pre_data.html', shifts=shifts)


@app.route('/submit_form/<form_id>', methods=['POST'])
def submit_form_data(form_id):
    return submit_form(form_id)


@app.route('/success')
def success():
    return "Form submitted successfully!"
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
