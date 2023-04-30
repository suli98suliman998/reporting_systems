from model import FormColumns, db, Form, Farm, Template


def get_form_columns_by_form_id(form_id):
    form_columns = db.session.query(FormColumns.column_title) \
        .filter(FormColumns.form_id == form_id) \
        .all()
    return [column[0] for column in form_columns]


def get_all_farms():
    farms = Farm.query.with_entities(Farm.farm_name).all()
    farm_list = [farm[0] for farm in farms]
    return farm_list


def get_form_by_id(form_id: int):
    form = Form.query.filter_by(form_id=form_id).first()
    f = Form(form_id=form.form_id, template_id=form.template_id, filled_by=form.filled_by, farm_name=form.farm_name,
             barn_number=form.barn_number, cycle_number=form.cycle_number, metadata_id=form.metadata_id)
    return f


def get_forms_by_cycle_number(cycle_number, farm_name, barn_number):
    forms = Form.query.filter_by(cycle_number=cycle_number, farm_name=farm_name, barn_number=barn_number).all
    return forms


def get_forms_by_farm_name_cycle_number_delivery_note(farm_name, cycle_number):
    forms = Form.query.filter_by(cycle_number=cycle_number, farm_name=farm_name).all
    return forms


