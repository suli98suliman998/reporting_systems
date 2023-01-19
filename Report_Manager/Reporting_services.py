import datetime
from flask import render_template, redirect
from Report_Manager import TemplateModel
from Report_Manager.FormModel import get_form_by_id
from Report_Manager.TemplateModel import get_row_titles_by_template_id
from User.UserModel import get_user_info
from model import Metadata, Form, FormColumns, TemplateRow, SubmittedData, db


def get_form(form_type: str, cycle_number, columns):
    template_id = TemplateModel.get_template_id_by_type(form_type)
    template_rows = get_row_titles_by_template_id(template_id)
    user = get_user_info(1)  # later using session
    filled_by = user["user_id"]
    farmName = user["farmName"]
    barnNumber = user['houseNu']
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
                           row_names=template_rows)


def submit_form(form_id):
    from flask import request
    if request.method == "POST":
        form = get_form_by_id(form_id)
        print(form)
        print("submit triggred")
        columns = get_row_titles_by_template_id(template_id=form.template_id)
        print(columns)
        column_titles = [column for column in columns]
        form_data = {}
        print(columns)
        print(column_titles)
        for column in column_titles:
            print(column)
            form_data[column] = request.form.get(column)
        form = Form.query.filter_by(form_id=form.form_id).first()
        template_id = form.template_id
        template_rows = FormColumns.query.filter_by(form_id=form_id).all()
        row_titles = [row.column_title for row in template_rows]
        for column in column_titles:
            for row in row_titles:
                data = request.form.get(row+"-"+column)
                print(template_id, column, form_id, row, data)
                submitted_data = SubmittedData(template_id=template_id, column_title=column, form_id=form.form_id, row_title=row, data=data)
                db.session.add(submitted_data)
                db.session.commit()
        return redirect("/success")
