from model import TemplateRow, db, template_rows_schema, Template


def get_row_titles_by_template_id(template_id):
    row_titles = db.session.query(TemplateRow.row_title) \
        .filter(TemplateRow.template_id == template_id) \
        .all()
    return [title[0] for title in row_titles]


def get_template_id_by_type(value):
    template = Template.query.filter_by(type=value).first()
    if template:
        return template.template_id
    else:
        return None
