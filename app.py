from flask import jsonify, render_template, request, url_for, redirect

from Report_Manager.FormModel import get_form_columns_by_form_id
from Report_Manager.Reporting_services import submit_form, get_form
from Report_Manager.TemplateModel import get_row_titles_by_template_id, get_template_id_by_type
from model import app, Farm


# @app.route('/labor_form/<shift>', methods=['GET', 'POST'])
# def view_labor_form(shift):
#     rows = get_row_titles_by_template_id(1)
#     print(rows)
#     print([shift])
#     return render_template('form_builder.html', column_names=[shift], row_names=rows)


@app.route('/labor_pre_form', methods=['GET', 'POST'])
def view_labor_pre_form():
    if request.method == 'POST':
        cycle_number = request.form.get("cycle_number")
        shift = request.form.get("shift")
        columns = [shift]
        return redirect(url_for('view_form', form_type='Daily_Barn', cycle_number=cycle_number, columns=columns))
    from Report_Manager.FormModel import get_form_columns_by_form_id
    shifts = get_form_columns_by_form_id(1)  # from form_coolumns

    return render_template('daily_barn_pre_data.html', shifts=shifts)


def get_all_farms():
    farms = Farm.query.with_entities(Farm.farm_name).all()
    farm_list = [farm[0] for farm in farms]
    print(farm_list)
    return farm_list


@app.route("/get_barn_count", methods=["POST"])
def get_barn_count():
    data = request.get_json()
    farm_name = data["farm_name"]
    farm = Farm.query.filter_by(farm_name=farm_name).first()
    barn_count = farm.total_barn_count if farm else 0
    return jsonify({"barn_count": barn_count})


@app.route('/supervisor_pre_form', methods=['GET', 'POST'])
def view_supervisor_pre_form():
    if request.method == 'POST':
        farm_name = request.form.get("farm_name")
        print(farm_name)
        cycle_number = request.form.get("cycle_number")
        barn_number = request.form.get("barn_number")
        columns = [barn_number]
        print(columns)
        return redirect(
            url_for('view_form', form_type='Daily_Farm_Supervisor', cycle_number=cycle_number, columns=columns))
    farms = get_all_farms()
    return render_template('daily_supervisor_pre_data.html', farms=farms)


@app.route('/tech_pre_form', methods=['GET', 'POST'])
def view_tech_pre_form():
    if request.method == 'POST':
        farm_name = request.form.get("farm_name")
        print(farm_name)
        cycle_number = request.form.get("cycle_number")
        barn_number = request.form.get("barn_number")
        columns = [barn_number]
        print(columns)
        return redirect(
            url_for('view_form', form_type='Daily_Farm_Tech', cycle_number=cycle_number, columns=columns))
    farms = get_all_farms()
    return render_template('daily_tech_pre_data.html', farms=farms)


# Daily_OP
@app.route('/op_pre_form', methods=['GET', 'POST'])
def view_op_pre_form():
    if request.method == 'POST':
        farm_name = request.form.get("farm_name")
        print(farm_name)
        cycle_number = request.form.get("cycle_number")
        barn_number = request.form.get("barn_number")
        columns = [barn_number]
        print(columns)
        return redirect(
            url_for('view_form', form_type='Daily_OP', cycle_number=cycle_number, columns=columns))
    farms = get_all_farms()
    return render_template('daily_op_pre_data.html', farms=farms)


@app.route('/farm_pre_form', methods=['GET', 'POST'])
def view_farm_pre_form():
    if request.method == 'POST':
        farm_name = request.form.get("farm_name")
        print(farm_name)
        cycle_number = request.form.get("cycle_number")
        barn_number = request.form.get("barn_number")
        columns = [barn_number]
        print(columns)
        return redirect(
            url_for('view_form', form_type='Daily_Farm', cycle_number=cycle_number, columns=columns))
    farms = get_all_farms()
    return render_template('daily_farm_pre_data.html', farms=farms)


# @app.route('/form/Daily_Farm_Supervisor', methods=['GET', 'POST'])
# def view_form(form_type='Daily_Farm_Supervisor'):
#     cycle_number = request.args.get('cycle_number')
#     columns = request.args.getlist('columns')
#     return get_form(form_type=form_type, cycle_number=cycle_number, columns=columns)


@app.route('/form/<form_type>', methods=['GET', 'POST'])
def view_form(form_type):
    cycle_number = request.args.get('cycle_number')
    columns = request.args.getlist('columns')
    return get_form(form_type=form_type, cycle_number=cycle_number, columns=columns)


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
