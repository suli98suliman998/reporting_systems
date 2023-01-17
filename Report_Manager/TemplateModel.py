from model import TemplateRow, db


def get_row_titles_by_template_id(template_id):
    row_titles = db.session.query(TemplateRow.row_title) \
        .filter(TemplateRow.template_id == template_id) \
        .all()
    return [title[0] for title in row_titles]

