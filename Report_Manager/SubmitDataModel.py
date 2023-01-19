from model import SubmittedData, db


def submit_data(template_id, row_title, form_id, column_title, data):
    submitted_data = SubmittedData(template_id=template_id, row_title=row_title, form_id=form_id, column_title=column_title, data=data)
    db.session.add(submitted_data)
    db.session.commit()

