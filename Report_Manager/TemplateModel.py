from model import TemplateRow, db, template_rows_schema


def get_row_titles_by_template_id(template_id):
    row_titles = db.session.query(TemplateRow.row_title) \
        .filter(TemplateRow.template_id == template_id) \
        .all()
    return [title[0] for title in row_titles]


def get_template_rows(template_id):
    rows = TemplateRow.query.filter_by(template_id=template_id).all()
    rows_info = template_rows_schema.dump(rows)
    return rows_info
