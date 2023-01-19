
def get_total_mortalties(data):
    sum = 0
    for i in data:
        sum = sum + int(i["Mortality"])
    return sum
