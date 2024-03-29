from model import TemplateRow, db, Template


def get_row_titles_by_template_id(template_id):
    row_titles = db.session.query(TemplateRow.row_title) \
        .filter(TemplateRow.template_id == template_id) \
        .order_by(TemplateRow.order) \
        .all()
    return [title[0] for title in row_titles]


def get_template_id_by_type(template_type):
    template = Template.query.filter_by(type=template_type).first()
    if template:
        return template.template_id
    else:
        return None
