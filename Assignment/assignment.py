# # import csv
# #
# # with open('stores.csv') as csv_file:
# #     csv_reader = csv.reader(csv_file, delimiter=',')
# #
# #     for row in csv_reader:
# #         print(row)
# #
# d = {1: [2, 3, 4], 2: [2, 3, 4, 5]}
# print(d)
# values = d.values()
# values_list = []
# print(values)
# for v in values:
#     values_list.append(v)
# for v in range(0, len(values_list) - 1):
#
#     cal = len(values_list[v])
#     cal_1 = len(values_list[v + 1])
#     if cal < cal_1:
#         max = values_list[v + 1]
#     else:
#         max = values_list[v]
# print(max)
# for key, value in d.items():
#
#     if max == value:
#         print(key)
import pandas as csv

stores = csv.read_csv('stores.csv', delimiter=',')
location = csv.read_csv('exercise_1_location.csv', delimiter=',')


def city_contain_z():
    city = location['city']
    store = stores['store_name']
    city_list = []
    d = {}
    result_dict = {}
    for names in city:
        city_list.append(names)
    length_city = len(city_list)
    for c in range(0, length_city - 1):
        if city_list[c] not in d.keys():
            d[city_list[c]] = store[c]
        else:
            d[city_list[c]] = d[city_list[c]] + ',' + str(store[c])
    print(d)
    values = d.values()
    values_list = []
    length_1 = []
    for v in values:
        values_list.append(v)
    for v in range(0, len(values_list)):
        length = len(values_list[v])
        length_1.append(length)
    print(length_1)
    for c in range(0, length_city - 1):
        if city_list[c] not in result_dict.keys():
            result_dict[city_list[c]] = length_1[c]
        else:
            result_dict[city_list[c]] = result_dict[city_list[c]] + ',' + length_1[c]

    print(result_dict)


city_contain_z()
