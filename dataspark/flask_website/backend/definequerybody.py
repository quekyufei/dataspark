#
# def create_age_filter(agelist):
#     if agelist != 'NA':
#         lower = agelist[0]
#         upper = agelist[1]
#
#         filter_string = "{\"type\": \"bound\", \"dimension\": \"agent_year_of_birth\", \"lower\": " + str \
#             (lower) + ", \"upper\": " + str(upper) +"}"
#
#         return filter_string
#
#
# def create_gender_filter(gender):
#     if gender != 'NA':
#         filter_string = "{\"type\": \"selector\", \"dimension\": \"agent_gender\", \"value\": \"" + str(gender) + "\"}"
#         return filter_string
#
#
# def create_race_filter(race):
#     if race != 'NA':
#         filter_string = "{\"type\": \"selector\", \"dimension\": \"agent_race\", \"value\": \"" + str(race) + "\"}"
#         return filter_string
#
#
# def create_nationality_filter(nationality):
#     if nationality != 'NA':
#         filter_string = "{\"type\": \"selector\", \"dimension\": \"agent_nationality\", \"value\": \"" + str(nationality) + "\"}"
#         return filter_string
import ast

def create_filter(key, value):
    if key == 'age':
        if value != 'NA':
            lower = value[0]
            upper = value[1]

            filter_string = "{\"type\": \"bound\", \"dimension\": \"agent_year_of_birth\", \"lower\": " + str \
                (lower) + ", \"upper\": " + str(upper) + "}"
            return filter_string

    elif key == 'gender':
        if value != 'NA':
            filter_string = "{\"type\": \"selector\", \"dimension\": \"agent_gender\", \"value\": \"" + str(
                value) + "\"}"
            return filter_string

    elif key == 'race':
        if value != 'NA':
            filter_string = "{\"type\": \"selector\", \"dimension\": \"agent_race\", \"value\": \"" + str(value) + "\"}"
            return filter_string

    elif key == 'nationality':
        if value == "SGP":
            filter_string = "{\"type\": \"selector\", \"dimension\": \"agent_nationality\", \"value\": \"" + str(
                value) + "\"}"
            return filter_string
        elif value == "OTHERS":
            filter_string = "{\"type\": \"NOT\", \"dimension\": \"agent_nationality\", \"value\": \"" + str(
                value) + "\"}"
            return filter_string


# print(create_age_filter([1990, 1995]))
# print(create_gender_filter('M'))
# print(create_race_filter('CHINESE'))


def main_filter_thing(dict_params):
    counter = 0
    for key, value in dict_params.items():
        if not value == 'NA':
            counter+= 1

    if counter == 0:
        return None
    elif counter == 1:
        return_string = '{"filter":'
        for key, value in dict_params.items():
            if not value == 'NA':
                return_string += create_filter(key, value) + "}"
                return ast.literal_eval(return_string)
    else:
        return_string = '{"filter": {"type": "and", ' \
                        '"fields": [' \
                        + create_filter('age', dict_params['age']) + ',' \
                        + create_filter('gender', dict_params['gender']) + ',' \
                        + create_filter('race', dict_params['race']) + ',' \
                        + create_filter('nationality', dict_params['nationality']) + ']}}'
        return ast.literal_eval(return_string)
        #need to add location to the return string


# main_filter_thing({"gender": "NA", "age": [1990, 1995], "race": "NA", "nationality": "NA"})

def main_filter_thing_OD(dict_params, i):
    counter = 0
    for key, value in dict_params.items():
        if not value == 'NA':
            counter += 1
    if counter == 0:
        return_string = '{"filter":' + "{\"type\": \"not\", \"field\": {\"type\": \"selector\", \"dimension\": \"origin_subzone\", \"value\":\"" + str(i) + "\"}}}"
        print(return_string + "counter 0")
        return ast.literal_eval(return_string)
    else:
        tempstring = "{\"type\": \"not\", \"field\": {\"type\": \"selector\", \"dimension\": \"origin_subzone\", \"value\":\"" + str(i) + "\"}}"
        print(tempstring)
        return_string = '{"filter": {"type": "and", ' \
                        '"field": [' \
                        + create_filter('age', dict_params['age']) + ',' \
                        + create_filter('gender', dict_params['gender']) + ',' \
                        + create_filter('race', dict_params['race']) + ',' \
                        + tempstring + '},' \
                        + create_filter('nationality', dict_params['nationality']) + ']}}'
        print(return_string)
        return ast.literal_eval(return_string)


# return_string = '{"filter":' + str({"type": "not", "field": {"type": "selecter", "dimension": "origin_subzone", "value": "CASZ02"}})+ "}"
# print(return_string)
# main_filter_thing_OD({"gender": "NA", "age": 'NA', "race": "NA", "nationality": "NA"}, "CASZ02")

