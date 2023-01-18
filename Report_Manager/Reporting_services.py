import datetime

from flask import render_template

from Report_Manager import TemplateModel
from Report_Manager.FormModel import get_form_columns_by_form_id
from Report_Manager.TemplateModel import get_row_titles_by_template_id
from User.UserModel import get_user_info
from model import Metadata, Form


def get_form(form_type: str):
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
    print(metadata.metadata_id)
    form = Form(template_id=template_id, filled_by=filled_by, farm_name=farmName, barn_number=barnNumber, cycle_number=None,
                metadata_id=int(metadata.metadata_id))
    form.save()
    form_columns = get_form_columns_by_form_id(template_id)
    return render_template('form_builder.html', column_names=form_columns, row_names=template_rows)




