from flask import request, redirect, url_for, render_template

from model import Users, Labor, db


def controller_create_user():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        jobTitle = request.form.get('jobTitle')

        new_user = Users(name=name, username=username, jobTitle=jobTitle)
        db.session.add(new_user)
        db.session.commit()
        if jobTitle == 'Labor':
            houseNu = request.form.get('houseNu')
            farmName = request.form.get('farmName')
            new_labor = Labor(user_id=new_user.user_id, houseNu=houseNu, farmName=farmName)
            new_labor.labor_save()

        return "Done"
    job_titles = ['Labor', 'Farm Supervisor', 'Farm Eng', 'Regional Manager', 'Operation Manager', 'COO', 'CEO',
                  'Sales Manager']
    return render_template('register_user.html', job_titles=job_titles)