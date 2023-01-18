import datetime

from flask import request, render_template

from Report_Manager.FormModel import get_form_columns_by_form_id
from Report_Manager.TemplateModel import get_row_titles_by_template_id


def controller_daily_barn_pre_form():
    if request.method == 'POST':
        cycle_number = request.form.get("cycle_number")
        shift = request.form.get("shift")
        date = datetime.date
        print(date)
        print(cycle_number)
        print(shift)
        column_names = get_form_columns_by_form_id(1)
        row_names = get_row_titles_by_template_id(1)
        return render_template('form_builder.html', column_names=column_names, row_names=row_names)
    shifts = ["6:00 -> 9:00", "9:00 -> 12:00", "12:00 -> 15:00", "15:00 -> 18:00"]
    return render_template('daily_barn_pre_data.html', shifts=shifts)