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
            print(filter_string)
            return filter_string

    elif key == 'gender':
        if value != 'NA':
            filter_string = "{\"type\": \"selector\", \"dimension\": \"agent_gender\", \"value\": \"" + str(
                value) + "\"}"
            print(filter_string)
            return filter_string

    elif key == 'race':
        if value != 'NA':
            filter_string = "{\"type\": \"selector\", \"dimension\": \"agent_race\", \"value\": \"" + str(value) + "\"}"
            print(filter_string)
            return filter_string

    elif key == 'nationality':
        if value == "SGP":
            filter_string = "{\"type\": \"selector\", \"dimension\": \"agent_nationality\", \"value\": \"" + str(
                value) + "\"}"
            print(filter_string)
            return filter_string
        elif value == "OTHERS":
            filter_string = "{\"type\": \"NOT\", \"dimension\": \"agent_nationality\", \"value\": \"" + str(
                value) + "\"}"
            print(filter_string)
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
        return_string = '"filter":'
        for key, value in dict_params.items():
            if not value == 'NA':
                return_string += create_filter(key, value)
                print(return_string)
                return ast.literal_eval(return_string)
    else:
        return_string = '"filter":{ "type": "and",' \
                        '"fields": [' \
                        + create_filter('age', dict_params['age']) + ',' \
                        + create_filter('gender', dict_params['gender']) + ',' \
                        + create_filter('race', dict_params['race']) + ',' \
                        + create_filter('nationality', dict_params['nationality']) + ']},'
        print(return_string)
        return ast.literal_eval(return_string)
        #need to add location to the return string


main_filter_thing({"gender": "M", "age": [1990, 1995], "race": "CHINESE", "nationality": "SGP"})