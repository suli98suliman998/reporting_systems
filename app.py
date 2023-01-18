from flask import jsonify, render_template, request

from Report_Manager.TemplateModel import get_row_titles_by_template_id

from model import app


@app.route('/template/<int:template_id>/rows')
def get_template_rows(template_id):
    row_titles = get_row_titles_by_template_id(template_id)

    return jsonify(row_titles)


@app.route('/labor_form')
def view_labor_form():
    columns = request.args.get("columns")
    rows = request.args.get("rows")
    return render_template('form_builder.html', column_names=columns, row_names=rows)


@app.route('/labor_pre_form', methods=['GET', 'POST'])
def view_labor_pre_form():
    from Report_Manager.FormController import controller_daily_barn_pre_form
    return controller_daily_barn_pre_form()


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/register_user', methods=['GET', 'POST'])
def view_user_registration():
    from User.UserController import controller_create_user
    return controller_create_user()


@app.route('/register_labor', methods=['GET', 'POST'])
def view_labor_registration():
    from User.UserController import controller_create_labor
    return controller_create_labor()


if __name__ == '__main__':
    app.run(debug=True)
