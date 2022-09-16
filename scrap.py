


def scrap_weather():
    # scrap weather data from a website
    # return a list of data
    # data = [(date1, temp1, hum1), (date2, temp2, hum2), (date3, temp3, hum3)]
    
    return data


def to sql_string(value_list):
    sql_string = ""
    for value in value_list:
        value = tuple(value)
        sql_string += str(value) + ","
    sql_string = sql_string[:-1]
    return sql_string


