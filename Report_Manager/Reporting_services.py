import datetime
from flask import render_template, redirect
from Report_Manager import TemplateModel
from Report_Manager.FormModel import get_form_by_id
from Report_Manager.SubmitDataModel import get_submitted_data
from Report_Manager.TemplateModel import get_row_titles_by_template_id
from User.UserModel import get_user_info
from model import Metadata, Form, FormColumns, TemplateRow, SubmittedData, db, Template


def get_data_for_farm(farm_name, cycle_number):
    forms = Form.query.filter_by(farm_name=farm_name, cycle_number=cycle_number, template_id=5).order_by(
        Form.form_id.desc()).all()
    if not forms:
        return {}
    submitted_data = {}
    for form in forms:
        form_id = form.form_id
        for SubmitedData in SubmittedData.query.filter_by(form_id=form_id).all():
            value = SubmitedData.data
            column_title = SubmitedData.column_title
            key = column_title
            if key == 'Total Occupation' or key == 'Total Mortalities':
                try:
                    submitted_data[key] = int(submitted_data[key]) + int(value)
                except:
                    submitted_data[key] = value
            elif key == 'Age':
                try:
                    if int(submitted_data[key]) < int(value):
                        submitted_data[key] = value
                except:
                    submitted_data[key] = value
            elif key == 'Left Chicks':
                try:
                    submitted_data[key] = int(submitted_data['Total Occupation']) - int(
                        submitted_data['Total Mortalities'])
                except:
                    submitted_data[key] = value
            else:
                submitted_data[key] = value
    return submitted_data


def translateToArabic(text):
    if text == 'qudaid':
        return 'قديد'


def get_value_for_row(data, row):
    if data == {}:
        return 'Nothing until now'
    elif row == 'Mortalities Percentage':
        total_mortalities = data['Total Mortalities']
        total_occupation = data['Total Occupation']
        mortality_percentage = (int(total_mortalities) / int(total_occupation)) * 100
        return mortality_percentage
    elif row == 'On Plan':
        return 'true'
    elif row == 'General Status':
        return 'Good'
    elif row == 'Farm Name':
        return "non"

    else:
        return data[row]


def build_totals_form(cycle_number):
    template_id = 6
    form_type = "Daily_Management"

    from Report_Manager.FormModel import get_all_farms
    farms = get_all_farms()

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

    form = Form(template_id=template_id, filled_by=filled_by, farm_name='General', barn_number='All',
                cycle_number=cycle_number, metadata_id=int(metadata.metadata_id))
    form.save()

    # Fetch the required data from the database and prepare it for rendering
    column_names = []  # List to store farm names for the header
    categories = {}  # Dictionary to store row data for each farm

    for farm in farms:
        column_names.append(farm)
        categories[farm] = []
        data = get_data_for_farm(farm, cycle_number)  # Fetch data for the given farm and cycle_number from the database
        for row in template_rows:
            value = get_value_for_row(data, row)  # Fetch the value for the given row from the fetched data
            categories[f"{farm}-{row}"] = value
    return render_template('totals.html', form_id=form.form_id, farms=farms, row_names=template_rows,
                           categories=categories)


def build_delivery_note_form(farmName, cycle_number):
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
    form = Form(template_id=template_id, filled_by=filled_by, farm_name=farmName, barn_number='0',
                cycle_number=cycle_number,
                metadata_id=int(metadata.metadata_id))
    form.save()
    column = farmName
    new_form_column = FormColumns(form_id=form.form_id, column_title=str(column))
    new_form_column.save()
    from categories.categoriesModel import get_categories
    categories = get_categories()
    return render_template('delivery_note.html', form_id=form.form_id, farm_name=farmName, row_names=template_rows,
                           column_names=[farmName], categories=categories)


def get_form(form_type: str, cycle_number, columns, farm_name, barn_number):
    template_id = TemplateModel.get_template_id_by_type(form_type)
    template_rows = get_row_titles_by_template_id(template_id)
    user = get_user_info(1)  # later using session
    filled_by = user["user_id"]
    farmName = farm_name
    barnNumber = barn_number
    date = datetime.datetime.now().date()
    time = int(datetime.datetime.now().time().hour.numerator)
    title = form_type
    rows_data = {}
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
    from templates.translator import translate_to_arabic, translate_to_english
    return render_template('form_builder.html', form_id=form.form_id, column_names=form_columns,
                           row_names=template_rows, rows_data=rows_data, translate_to_arabic=translate_to_arabic,
                           translate_to_english=translate_to_english)


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
                db.session.add(submitted_data)
                db.session.commit()
        return redirect("/success")


def get_total_mortality(cycle_number, farm_name, barn_number):
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
    from Buisness_Logic.calculate_totals import set_max_age
    forms_data = set_max_age(forms_data)
    return forms_data


def get_forms_of_type(farm_name, barn_number, cycle_number, template_type):
    template = Template.query.filter_by(type=template_type).first()
    template_id = template.template_id
    forms = Form.query.filter_by(template_id=template_id, cycle_number=cycle_number, farm_name=farm_name,
                                 barn_number=barn_number).all()
    forms = [forms, template_id]
    return forms


def get_date_time(metadata_id):
    metadata = Metadata.query.filter_by(metadata_id=metadata_id).first()
    date = metadata.date
    time = metadata.time
    return date, time
