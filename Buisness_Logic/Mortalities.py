
def get_total_of_specefic_row(data, needed_data="Consumed Feed"):
    sum = 0
    for i in data:
        sum = sum + int(i[needed_data])
    return sum
