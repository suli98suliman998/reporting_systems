from model import FormColumns, db


def get_form_columns_by_form_id(form_id):
    form_columns = db.session.query(FormColumns.column_title) \
        .filter(FormColumns.form_id == form_id) \
        .all()
    return [column[0] for column in form_columns]