import datetime

from flask import jsonify, render_template, request, url_for, redirect
from model import app, Farm, Form, TemplateRow, FormColumns


def get_hour(time_string):
    return int(time_string.split(':')[0])


def is_between(shift):
    current_time = datetime.datetime.now().hour
    start_time, end_time = shift.split(" to ")
    start_hour = int(start_time.split(':')[0])
    end_hour = int(end_time.split(':')[0])
    print(start_hour)
    print(end_hour)
    if start_hour <= end_hour:
        return start_hour <= current_time <= end_hour
    else:  # start_hour > end_hour, assuming end hour is next day
        return current_time >= start_hour or current_time <= end_hour


@app.route('/labor_pre_form', methods=['GET', 'POST'])
def view_labor_pre_form():
    import cv2
    cap = None
    shifts = ['3:00 -> 6:00', '6:00 -> 9:00', '9:00 -> 12:00', '12:00 -> 15:00', '15:00 -> 18:00', '18:00 -> 21:00',
              '21:00 -> 24:00', '24:00 -> 3:00']
    from Report_Manager.Reporting_services import get_shift
    shift = get_shift(shifts)
    if request.method == 'POST':
        cap = cv2.VideoCapture(0)
        while True:
            _, frame = cap.read()
            decoded_data, _, _ = cv2.QRCodeDetector().detectAndDecode(frame)
            if decoded_data:
                data = decoded_data
                farm_name, barn_number, cycle_number = data.split(",")
                farm_name = farm_name.split(":")[1]
                barn_number = barn_number.split(":")[1]
                cycle_number = cycle_number.split(":")[1]
                print(farm_name)
                print(cycle_number)
                print(barn_number)
                print(shift)
                columns = [shift]
                return redirect(
                    url_for('view_labor_form', form_type='Daily_Barn', farm_name=farm_name, barn_number=barn_number,
                            cycle_number=cycle_number, columns=columns))
            cv2.imshow("Webcam", frame)
            key = cv2.waitKey(1)
            if key == 27:
                break
    if cap:
        cap.release()
    cv2.destroyAllWindows()
    return render_template('daily_barn_pre_data.html')


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
    from Report_Manager.FormModel import get_all_farms
    farms = get_all_farms()
    return render_template('daily_supervisor_pre_data.html')


@app.route('/generate_qr', methods=['GET', 'POST'])
def generate_qr():
    if request.method == 'GET' or request.method == 'POST':
        farm_name = request.form.get('farm_name')
        barn_number = request.form.get('barn_number')
        cycle_number = request.form.get('cycle_number')
        from Report_Manager.Reporting_services import generate_qr_code
        generate_qr_code(cycle_number, farm_name, barn_number)
        return render_template('make_qr.html')


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
    from Report_Manager.FormModel import get_all_farms
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
    from Report_Manager.FormModel import get_all_farms
    farms = get_all_farms()
    return render_template('daily_farm_pre_data.html', farms=farms)


@app.route('/form/<form_type>', methods=['GET', 'POST'])
def view_form(form_type):
    cycle_number = request.args.get('cycle_number')
    columns = request.args.getlist('columns')
    from Report_Manager.Reporting_services import get_form
    return get_form(form_type=form_type, cycle_number=cycle_number, columns=columns)


@app.route('/submit_form/<form_id>', methods=['POST'])
def submit_form_data(form_id):
    from Report_Manager.Reporting_services import submit_form
    return submit_form(form_id)


@app.route('/success')
def success():
    return "Form submitted successfully!"


@app.route('/get_data/<cycle_number>/<farm_name>/<barn_number>', methods=['GET', 'POST'])
def get_forms_data(cycle_number, farm_name, barn_number):
    form_data = {}
    forms_data = []
    forms = Form.query.filter_by(cycle_number=cycle_number, farm_name=farm_name, barn_number=barn_number).all()
    print(forms)
    for form in forms:
        template_id = form.template_id
        template_rows = TemplateRow.query.filter_by(template_id=template_id).all()
        form_columns = FormColumns.query.filter_by(form_id=form.form_id).all()
        for form_column in form_columns:
            for template_row in template_rows:
                row = TemplateRow.query.filter_by(template_id=form.template_id,
                                                  row_title=template_row.row_title).first()
                from Report_Manager.SubmitDataModel import get_submitted_data
                data = get_submitted_data(template_id=template_row.template_id,
                                          row_title=form_column.column_title, form_id=form.form_id,
                                          column_title=row.row_title)
                form_data[template_row.row_title] = data
            forms_data.append(form_data)

            form_data = {}

    print(forms_data)
    from Buisness_Logic.Mortalities import get_total_of_specefic_row
    total_mortality = str(
        "Total mortality for farm: " + farm_name + " cycle number: " + str(cycle_number) + " in barn number " + str(
            barn_number) + "is" + str(get_total_of_specefic_row(forms_data)))
    return total_mortality


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
