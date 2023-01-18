from flask import request, redirect, url_for, render_template

from model import Users, Labor, db


def controller_create_labor():
    if request.method == 'POST':
        print("11s")
        name = request.form.get('name')
        username = request.form.get('username')
        farmName = request.form.get("farmName")
        barnNumber = request.form.get("houseNu")
        from User.UserModel import db_create_labor
        db_create_labor(name, username, farmName, barnNumber)
        return "Done"
    job_titles = ['Farm Supervisor', 'Farm Eng', 'Regional Manager', 'Operation Manager', 'COO', 'CEO',
                  'Sales Manager']
    return render_template('register_labor.html', job_titles=job_titles)


def controller_create_user():
    if request.method == 'POST':
        print(111111)
        name = request.form.get('name')
        username = request.form.get('username')
        jobTitle = request.form.get('jobTitle')
        from User.UserModel import db_create_user
        db_create_user(name, username, jobTitle)
        return "Done"
    job_titles = ['Farm Supervisor', 'Farm Eng', 'Regional Manager', 'Operation Manager', 'COO', 'CEO',
                  'Sales Manager']
    return render_template('register_user.html', job_titles=job_titles)