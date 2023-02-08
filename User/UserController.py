from flask import request, redirect, url_for, render_template

from model import Users, Labor, db


def controller_create_labor():
    if request.method == 'POST':
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
        name = request.form.get('name')
        username = request.form.get('username')
        jobTitle = request.form.get('jobTitle')
        from User.UserModel import db_create_user
        db_create_user(name, username, jobTitle)
        return "Done"
    job_titles = ['Farm Supervisor', 'Farm Eng', 'Regional Manager', 'Operation Manager', 'COO', 'CEO',
                  'Sales Manager']
    return render_template('register_user.html', job_titles=job_titles)


def controller_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        from User.UserModel import db_login
        user = db_login(username, password)
        if user:
            from flask import session
            session['user_id'] = user.user_id
            session['username'] = user.username
            if user.jobTitle == "Labor":
                return redirect(url_for('labor_dashboard'))
            else:
                return redirect(url_for('dashboard'))
        else:
            return "Invalid username or password"
    return render_template('login.html')
