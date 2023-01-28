
def get_total_of_specefic_row(data, needed_data):
    total = 0
    if data:
        for i in data:
            if needed_data in i:
                try:
                    total = total + float(i[needed_data])
                except ValueError:
                    pass
    else:
        return None
    return total
