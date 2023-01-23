def get_labor_form(form_type: str, farm_name, barn_number, cycle_number, columns):
    template_id = TemplateModel.get_template_id_by_type(form_type)
    template_rows = get_row_titles_by_template_id(template_id)
    user = get_user_info(1)  # later using session
    filled_by = user["user_id"]
    farmName = farm_name
    barnNumber = barn_number
    date = datetime.datetime.now().date()
    time = int(datetime.datetime.now().time().hour.numerator)
    title = form_type
    metadata = Metadata(date=date, time=time, title=title)
    metadata.save()
    form = Form(template_id=template_id, filled_by=filled_by, farm_name=farmName, barn_number=barnNumber,
                cycle_number=cycle_number,
                metadata_id=int(metadata.metadata_id))
    form.save()
    form_columns = columns
    for column in form_columns:
        new_form_column = FormColumns(form_id=form.form_id, column_title=column)
        new_form_column.save()
    return render_template('form_builder.html', form_id=form.form_id, column_names=form_columns,
                           row_names=template_rows)
