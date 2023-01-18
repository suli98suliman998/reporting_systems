import datetime

from flask import request, render_template, redirect, url_for

import model


def controller_daily_barn_pre_form():
    if request.method == 'POST':
        cycle_number = request.form.get("cycle_number")
        shift = request.form.get("shift")
        date = datetime.date.today()
        time = "7:00"
        filled_by = 1  # current session user id
        from User.UserModel import get_user_info
        user = get_user_info(filled_by)
        print(user['farmName'])
        farmName = user['farmName']
        barnNumber = user['houseNu']
        print(farmName)
        print(barnNumber)
        print(date)
        print(cycle_number)
        print(shift)
        metadata = model.Metadata(date, str(time), "Daily Barn") # daily barn thorugh template id
        model.db.session.add(metadata)
        model.db.session.commit()
        metadata_id = metadata.metadata_id
        form = model.Form(template_id=1, filled_by=filled_by, farm_name=farmName, barn_number=int(barnNumber), cycle_number=cycle_number,
                          metadata_id=metadata_id)
        form.save()
        # row_names = get_row_titles_by_template_id(1)
        return redirect(url_for('view_labor_form', shift=shift))
    shifts = ["6:00 -> 9:00", "9:00 -> 12:00", "12:00 -> 15:00", "15:00 -> 18:00"] # from form_coolumns
    return render_template('daily_barn_pre_data.html', shifts=shifts)
