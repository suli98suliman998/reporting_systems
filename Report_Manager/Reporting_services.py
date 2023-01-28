import datetime
from flask import render_template, redirect
from Report_Manager import TemplateModel
from Report_Manager.FormModel import get_form_by_id
from Report_Manager.SubmitDataModel import get_submitted_data
from Report_Manager.TemplateModel import get_row_titles_by_template_id
from User.UserModel import get_user_info
from model import Metadata, Form, FormColumns, TemplateRow, SubmittedData, db, Template


def build_delivery_note_form(farmName, cycle_number):
    print(1)
    template_id = 10
    form_type = "Delivery_Note"
    from Report_Manager.TemplateModel import get_row_titles_by_template_id
    template_rows = get_row_titles_by_template_id(template_id)
    from User.UserModel import get_user_info
    user = get_user_info(1)  # later using session
    filled_by = user["user_id"]
    date = datetime.datetime.now().date()
    time = int(datetime.datetime.now().time().hour.numerator)
    title = form_type
    metadata = Metadata(date=date, time=time, title=title)
    metadata.save()
    print(111)
    form = Form(template_id=template_id, filled_by=filled_by, farm_name=farmName, barn_number='0',
                cycle_number=cycle_number,
                metadata_id=int(metadata.metadata_id))
    form.save()
    column = farmName
    new_form_column = FormColumns(form_id=form.form_id, column_title=str(column))
    new_form_column.save()
    print(farmName)
    return render_template('delivery_note.html', farm_name=farmName,
                           row_names=template_rows)


def get_form(form_type: str, cycle_number, columns):
    from Buisness_Logic.calculate_totals import get_total_of_specefic_row
    template_id = TemplateModel.get_template_id_by_type(form_type)
    template_rows = get_row_titles_by_template_id(template_id)
    user = get_user_info(1)  # later using session
    filled_by = user["user_id"]
    farmName = user["farmName"]
    barnNumber = user['houseNu']
    date = datetime.datetime.now().date()
    time = int(datetime.datetime.now().time().hour.numerator)
    title = form_type
    rows_data = {}
    data = get_data(farm_name=farmName, barn_number=barnNumber, cycle_number=cycle_number)
    for i in template_rows:
        for k in data:
            if k.get(i) is None:
                continue
            else:
                sum = get_total_of_specefic_row(data, i)
                rows_data[i] = sum
            break
    metadata = Metadata(date=date, time=time, title=title)
    metadata.save()
    form = Form(template_id=template_id, filled_by=filled_by, farm_name=farmName, barn_number=barnNumber,
                cycle_number=cycle_number,
                metadata_id=int(metadata.metadata_id))
    form.save()
    form_columns = columns
    for column in form_columns:
        new_form_column = FormColumns(form_id=form.form_id, column_title=column)
        new_form_column.save()
    return render_template('form_builder.html', form_id=form.form_id, column_names=form_columns,
                           row_names=template_rows, rows_data=rows_data)


def get_labor_form(form_type, farm_name, barn_number, cycle_number, columns):
    template_id = TemplateModel.get_template_id_by_type(form_type)
    template_rows = get_row_titles_by_template_id(template_id)
    user = get_user_info(1)  # later using session
    filled_by = user["user_id"]
    farmName = farm_name
    barnNumber = barn_number
    date = datetime.datetime.now().date()
    time = int(datetime.datetime.now().time().hour.numerator)
    title = form_type
    metadata = Metadata(date=date, time=time, title=title)
    metadata.save()
    form = Form(template_id=template_id, filled_by=filled_by, farm_name=farmName, barn_number=barnNumber,
                cycle_number=cycle_number,
                metadata_id=int(metadata.metadata_id))
    form.save()
    form_columns = columns
    for column in form_columns:
        new_form_column = FormColumns(form_id=form.form_id, column_title=column)
        new_form_column.save()
    return render_template('form_builder.html', form_id=form.form_id, column_names=form_columns,
                           row_names=template_rows, rows_data={})


def submit_form(form_id):
    from flask import request
    if request.method == "POST":
        form = get_form_by_id(form_id)
        columns = get_row_titles_by_template_id(template_id=form.template_id)
        column_titles = [column for column in columns]
        template_id = form.template_id
        template_rows = FormColumns.query.filter_by(form_id=form_id).all()
        row_titles = [row.column_title for row in template_rows]
        for column in column_titles:
            for row in row_titles:
                form_data = {}
                data = form_data[column] = request.form.get(column + "-" + row)
                submitted_data = SubmittedData(template_id=template_id, column_title=column, form_id=form.form_id,
                                               row_title=row, data=data)
                # print(form_data.popitem()[0])  # prints AVG Weight and [1] prints its value *******************
                db.session.add(submitted_data)
                db.session.commit()
        return redirect("/success")


def get_total_mortality(cycle_number, farm_name, barn_number):
    # Query the forms table for forms with the specified cycle number, farm name, and barn number
    forms = Form.query.filter_by(cycle_number=cycle_number, farm_name=farm_name, barn_number=barn_number).all()
    total_mortality = 0
    for form in forms:
        total_mortality += form.mortality
    return total_mortality


def get_shift():
    current_time = datetime.datetime.now().time()
    shifts = ['3:00 -> 6:00', '6:00 -> 9:00', '9:00 -> 12:00', '12:00 -> 15:00', '15:00 -> 18:00', '18:00 -> 21:00',
              '21:00 -> 24:00', '24:00 -> 3:00']

    if datetime.time(3, 0) <= current_time < datetime.time(6, 0):
        shift = shifts[0]
    elif datetime.time(6, 0) <= current_time < datetime.time(9, 0):
        shift = shifts[1]
    elif datetime.time(9, 0) <= current_time < datetime.time(12, 0):
        shift = shifts[2]
    elif datetime.time(12, 0) <= current_time < datetime.time(15, 0):
        shift = shifts[3]
    elif datetime.time(15, 0) <= current_time < datetime.time(18, 0):
        shift = shifts[4]
    elif datetime.time(18, 0) <= current_time < datetime.time(21, 0):
        shift = shifts[5]
    elif datetime.time(21, 0) <= current_time < datetime.time(0, 0):
        shift = shifts[6]
    else:
        shift = shifts[7]

    print(shift)
    return shift


def generate_qr_code(cycle_number, farm_name, barn_number):
    import qrcode
    data = f'Cycle Number:{cycle_number}, Farm Name:{farm_name}, Barn Number:{barn_number}'
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(f'qr_code_{farm_name}_{barn_number}_{cycle_number}.png')
    print(f'QR code image saved as qr_code_{farm_name}_{barn_number}_{cycle_number}.png in the project directory')


def get_data(farm_name, barn_number, cycle_number):
    form_data = {}
    forms_data = []
    forms = Form.query.filter_by(farm_name=farm_name, barn_number=barn_number,
                                 cycle_number=cycle_number).all()
    if forms:
        for form in forms:
            template_id = form.template_id
            form_rows = TemplateRow.query.filter_by(template_id=template_id).all()
            form_columns = FormColumns.query.filter_by(form_id=form.form_id).all()
            for form_column in form_columns:
                for form_row in form_rows:
                    data = get_submitted_data(template_id=form.template_id,
                                              row_title=form_column.column_title,
                                              form_id=form.form_id,
                                              column_title=form_row.row_title)
                    if data is not None:
                        try:
                            form_data[form_row.row_title] = float(data)
                        except ValueError:
                            form_data[form_row.row_title] = data
                forms_data.append(form_data)
                form_data = {}
    else:
        return None
    return forms_data


