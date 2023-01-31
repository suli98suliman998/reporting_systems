# def get_total_of_specefic_row(data, needed_data):
#     total = 0
#     if data:
#         for i in data:
#             if needed_data in i:
#                 try:
#                     total = total + float(i[needed_data])
#                 except ValueError:
#                     pass
#     else:
#         return None
#     return total
def get_total_of_specefic_row(data, needed_data):
    total = 0
    last_entered_value = None
    total_mortality = float()
    if data:
        for i in data:
            if needed_data in i:
                if needed_data in ["Mortality", "Consumed Water", "Consumed Feed", "Light Time"]:
                    try:
                        total += float(i[needed_data])
                        if needed_data in ["Mortality", "First Week Mortalities", "Arrived Mortalities"]:
                            total_mortality += float(i[needed_data])
                    except (ValueError, TypeError):
                        pass
                elif needed_data in ["Temperature", "AVG Weight", "PH Level"]:
                    if i[needed_data] and i[needed_data] != 0.0:
                        last_entered_value = i[needed_data]
                elif needed_data == "Age":
                    try:
                        age = float(i[needed_data])
                        total = max(age, total)
                    except (ValueError, TypeError):
                        pass
                elif needed_data == "Total Mortalities":
                    try:
                        total = total_mortality
                    except (ValueError, TypeError):
                        pass
                else:
                    try:
                        total += float(i[needed_data])
                    except (ValueError, TypeError):
                        pass
    else:
        return None
    if total == 0 and total_mortality > 0:
        return total_mortality
    else:
        return last_entered_value if needed_data in ["Temperature", "AVG Weight", "PH Level"] else total


def set_max_age(forms_data):
    max_age = 0
    for form_data in forms_data:
        if "Age" in form_data:
            try:
                age = float(form_data["Age"])
                if age > max_age:
                    max_age = age
            except ValueError:
                pass
    for form_data in forms_data:
        if "Age" in form_data:
            try:
                age = float(form_data["Age"])
                if age != max_age:
                    form_data["Age"] = 0
            except ValueError:
                form_data["Age"] = 0
    return forms_data


def set_avg_weight(forms_data):
    total_weight = 0.0
    count = 0
    for form_data in forms_data:
        if "AVG Weight" in form_data:
            try:
                total_weight += float(form_data["AVG Weight"])
                count += 1
            except ValueError:
                pass
    avg_weight = total_weight / count
    for form_data in forms_data:
        if "AVG Weight" in form_data:
            value = avg_weight / count
            form_data["AVG Weight"] = value
    return forms_data

# def validate_submitted_data(template_id, row_name, entered_value, calculated_value):
