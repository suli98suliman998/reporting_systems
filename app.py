from flask import jsonify, render_template, request

from Report_Manager.FormModel import get_form_columns_by_form_id
from Report_Manager.TemplateModel import get_row_titles_by_template_id
from User import UserModel

from model import app, db, Users, Labor


@app.route('/template/<int:template_id>/rows')
def get_template_rows(template_id):
    row_titles = get_row_titles_by_template_id(template_id)

    return jsonify(row_titles)


@app.route('/form/<int:form_id>')
def build_form(form_id):
    column_names = get_form_columns_by_form_id(form_id)
    for i in column_names:
        print(i)
    row_names = get_row_titles_by_template_id(form_id)
    return render_template('form_builder.html', column_names=column_names, row_names=row_names)


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/register_user', methods=['GET', 'POST'])
def view_user_registration():
    if request.method == 'POST':
        print(111111)
        name = request.form.get('name')
        username = request.form.get('username')
        jobTitle = request.form.get('jobTitle')
        UserModel.db_create_user(name, username, jobTitle)
        return "Done"
    job_titles = ['Farm Supervisor', 'Farm Eng', 'Regional Manager', 'Operation Manager', 'COO', 'CEO',
                  'Sales Manager']
    return render_template('register_user.html', job_titles=job_titles)


@app.route('/register_labor', methods=['GET', 'POST'])
def view_labor_registration():
    print(11)
    if request.method == 'POST':
        print("11s")
        name = request.form.get('name')
        username = request.form.get('username')
        farmName = request.form.get("farmName")
        barnNumber = request.form.get("houseNu")
        UserModel.db_create_labor(name, username, farmName, barnNumber)
        return "Done"
    job_titles = ['Farm Supervisor', 'Farm Eng', 'Regional Manager', 'Operation Manager', 'COO', 'CEO',
                  'Sales Manager']
    return render_template('register_labor.html', job_titles=job_titles)


if __name__ == '__main__':
    app.run(debug=True)
