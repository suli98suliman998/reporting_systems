from flask import jsonify, render_template, request, url_for, redirect
from model import app, Farm, Metadata, SubmittedData


# def get_hour(time_string):
#     return int(time_string.split(':')[0])
#
#
# def is_between(shift):
#     current_time = datetime.datetime.now().hour
#     start_time, end_time = shift.split(" to ")
#     start_hour = int(start_time.split(':')[0])
#     end_hour = int(end_time.split(':')[0])
#     print(start_hour)
#     print(end_hour)
#     if start_hour <= end_hour:
#         return start_hour <= current_time <= end_hour
#     else:  # start_hour > end_hour, assuming end hour is next day
#         return current_time >= start_hour or current_time <= end_hour

@app.route("/get_barn_count", methods=["POST"])
def get_barn_count():
    data = request.get_json()
    farm_name = data["farm_name"]
    farm = Farm.query.filter_by(farm_name=farm_name).first()
    barn_count = farm.total_barn_count if farm else 0
    return jsonify({"barn_count": barn_count})


@app.route('/generate_qr', methods=['GET', 'POST'])
def generate_qr():
    if request.method == 'GET' or request.method == 'POST':
        farm_name = request.form.get('farm_name')
        barn_number = request.form.get('barn_number')
        cycle_number = request.form.get('cycle_number')
        from Report_Manager.Reporting_services import generate_qr_code
        generate_qr_code(cycle_number, farm_name, barn_number)
        return render_template('make_qr.html')


@app.route('/labor_pre_form', methods=['GET', 'POST'])
def view_labor_pre_form():
    from Report_Manager.Reporting_services import get_shift
    shift = get_shift()
    if request.method == 'POST':
        from functions import read_qr_code
        cycle_number, farm_name, barn_number = read_qr_code()
        columns = [shift]
        return redirect(
            url_for('view_labor_form', form_type='Daily_Barn', farm_name=farm_name, barn_number=barn_number,
                    cycle_number=cycle_number, columns=columns))
    return render_template('daily_barn_pre_data.html')


@app.route('/supervisor_pre_form', methods=['GET', 'POST'])
def view_supervisor_pre_form():
    # add the measurement of the data
    if request.method == 'POST':
        farm_name = request.form.get("farm_name")
        print(farm_name)
        cycle_number = request.form.get("cycle_number")
        barn_number = request.form.get("barn_number")
        columns = [barn_number]
        print(columns)
        return redirect(
            url_for('view_form', form_type='Daily_Farm_Supervisor', cycle_number=cycle_number, columns=columns))
    from Report_Manager.FormModel import get_all_farms
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
    from Report_Manager.FormModel import get_all_farms
    farms = get_all_farms()
    return render_template('daily_tech_pre_data.html', farms=farms)


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
    from Report_Manager.FormModel import get_all_farms
    farms = get_all_farms()
    return render_template('daily_op_pre_data.html', farms=farms)


@app.route('/farm_pre_form', methods=['GET', 'POST'])
def view_farm_pre_form():
    if request.method == 'POST':
        farm_name = request.form.get("farm_name")
        cycle_number = request.form.get("cycle_number")
        barn_number = request.form.get("barn_number")
        columns = [barn_number]
        return redirect(
            url_for('view_form', form_type='Daily_Farm', cycle_number=cycle_number, columns=columns))
    from Report_Manager.FormModel import get_all_farms
    farms = get_all_farms()
    return render_template('daily_farm_pre_data.html', farms=farms)


@app.route('/form/labor', methods=['GET', 'POST'])
def view_labor_form():
    farm_name = request.args.get('farm_name')
    cycle_number = request.args.get('cycle_number')
    columns = request.args.getlist('columns')
    barn_number = request.args.get('barn_number')
    from Report_Manager.Reporting_services import get_labor_form
    return get_labor_form(form_type='Daily_Barn', farm_name=farm_name, barn_number=barn_number,
                          cycle_number=cycle_number,
                          columns=columns)


@app.route('/form/<form_type>', methods=['GET', 'POST'])
def view_form(form_type):
    cycle_number = request.args.get('cycle_number')
    columns = request.args.getlist('columns')
    from Report_Manager.Reporting_services import get_form
    print(columns)
    return get_form(form_type=form_type, cycle_number=cycle_number, columns=columns)


@app.route('/submit_form/<form_id>', methods=['POST'])
def submit_form_data(form_id):
    from Report_Manager.Reporting_services import submit_form
    return submit_form(form_id)


@app.route('/success')
def success():
    return redirect(url_for('home'))


@app.route('/delivery_note_pre_form', methods=['GET', 'POST'])
def view_delivery_note_pre_form():
    if request.method == 'POST':
        farm_name = request.form.get("farm_name")
        cycle_number = request.form.get("cycle_number")
        print("11", farm_name)
        return redirect(
            url_for('view_delivery_note_form', farm_name=farm_name, cycle_number=cycle_number))
    from Report_Manager.FormModel import get_all_farms
    farms = get_all_farms()
    return render_template('delivery_note_pre_form.html', farms=farms)


@app.route('/form/delivery_note', methods=['GET', 'POST'])
def view_delivery_note_form():
    farm_name = request.args.get('farm_name')
    cycle_number = request.args.get('cycle_number')
    print(farm_name)
    print(cycle_number)
    from Report_Manager.Reporting_services import build_delivery_note_form
    return build_delivery_note_form(farmName=farm_name,
                                    cycle_number=cycle_number)


@app.route('/view_data', methods=['GET', 'POST'])
def view_data():
    farm_name = request.form.get('farm_name')
    cycle_number = request.form.get('cycle_number')
    barn_number = request.form.get("barn_number")
    data_choice = request.form.get("data")
    print(farm_name)
    from Report_Manager.Reporting_services import get_data
    data = get_data(farm_name=farm_name, barn_number=barn_number, cycle_number=cycle_number)
    from Buisness_Logic.calculate_totals import get_total_of_specefic_row
    ttl = get_total_of_specefic_row(data, data_choice)
    msg = str(str(data_choice) + " is " + str(ttl))
    print(msg)
    from Report_Manager.FormModel import get_all_farms
    farms = get_all_farms()
    return render_template('review_data.html', farmName=farm_name,
                           cycle_number=cycle_number,
                           barn_number=barn_number,
                           data=data_choice,
                           farms=farms, msg=msg)


@app.route('/get_data', methods=['GET', 'POST'])
def get_form_data():
    if request.method == 'POST':
        farm_name = request.form.get('farm_name')
        barn_number = request.form.get('barn_number')
        cycle_number = request.form.get('cycle_number')
        needed_data = request.form.get('needed_data')
        from Report_Manager.Reporting_services import get_data
        data = get_data(farm_name=farm_name, barn_number=barn_number, cycle_number=cycle_number)
        print(data)
        from Buisness_Logic.calculate_totals import get_total_of_specefic_row
        result = get_total_of_specefic_row(data=data, needed_data=needed_data)
        print(result)
        return str(result)
    return render_template("search_for_data.html")


@app.route('/get_forms_data', methods=['GET', 'POST'])
def get_forms_data():
    if request.method == 'POST':
        farm_name = request.form.get('farm_name')
        barn_number = request.form.get('barn_number')
        cycle_number = request.form.get('cycle_number')
        template_type = request.form.get('template_type')
        from Report_Manager.Reporting_services import get_forms_of_type
        forms = get_forms_of_type(farm_name=farm_name, barn_number=barn_number, cycle_number=cycle_number,
                                  template_type=template_type)
        from Report_Manager.Reporting_services import get_date_time
        return render_template('table_of_forms.html', forms=forms, get_date_time=get_date_time)
    from Report_Manager.FormModel import get_all_farms
    farms = get_all_farms()
    return render_template("get_forms.html", farms=farms)


@app.route('/view_form_id/<form_id>', methods=['GET'])
def view_form_id(form_id):
    submitted_data = SubmittedData.query.filter_by(form_id=form_id).all()
    return render_template("view_form_id.html", submitted_data=submitted_data)


@app.route('/')
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
