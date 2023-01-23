from model import SubmittedData, db


def submit_data(template_id, row_title, form_id, column_title, data):
    submitted_data = SubmittedData(template_id=template_id, row_title=row_title, form_id=form_id,
                                   column_title=column_title, data=data)
    db.session.add(submitted_data)
    db.session.commit()


def get_submitted_data(template_id, row_title, form_id, column_title):
    submitted_data = SubmittedData.query.filter_by(template_id=template_id, row_title=row_title, form_id=form_id,
                                                   column_title=column_title).first()
    if submitted_data:
        return submitted_data.data
    else:
        return 0
