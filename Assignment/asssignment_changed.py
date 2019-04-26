import pandas as csv
from collections import Counter
import datetime as dt
import calendar

stores = csv.read_csv('stores.csv', delimiter=',')
location = csv.read_csv('exercise_1_location.csv', delimiter=',')
store = stores['store_name']
date_of_opening = stores['date_of_opening']
build_area = stores['build_area']
city = location['city']
pincode_stores = stores['pincode']
country = location['country']
pincode = location['pincode']


def build_area_4000():
    output_1 = stores['store_name'][stores['build_area'] >= 4000]
    print(output_1)


build_area_4000()


def country_pincode():
    dictionary = {}
    for key, value in zip(country, pincode):
        if key in dictionary:
            dictionary[key].append(value)
        else:
            dictionary[key] = [value]
    print(dictionary)

    dic = Counter(pincode_stores)
    dict1 = dict(dic)
    print(dict1)

    output = []
    for key, value in dictionary.items():
        for key2, value2 in dict1.items():
            if len(value) > 1:
                for i in value:
                    if key2 == i:
                        output.append(value2)
                        dictionary[key] = sum(output)
    print(dictionary)
    for key, value in dictionary.items():
        maxi = max(dictionary.values())
        if maxi == value:
            print(key)


country_pincode()


def total_build_area():
    dictionary = {}
    build_area_list = []
    for key, value in zip(date_of_opening, build_area):
        if key in dictionary:
            dictionary[key].append(value)
        else:
            dictionary[key] = [value]
    print(dictionary)
    today = date.today()
    this_year = today.year
    prev_year = this_year - 1
    for key, value in dictionary.items():
        month, day, year = (int(x) for x in key.split('/'))
        year = year
        if prev_year == year:
            build_area_list.append(value)
    result = []
    for sub_list in build_area_list:
        for i in sub_list:
            result.append(i)
    print(sum(result))


total_build_area()


def saturday_sunday():
    dictionary = {}
    result = []
    for key, value in zip(store, date_of_opening):
        if key not in dictionary:
            dictionary[key] = value
    for key, value in dictionary.items():
        month, day, year = (dt.datetime(x) for x in value.split('/'))
        my_date = dt.date(month, day, year)
        print(calendar.day_name[my_date.weekday()])
        if calendar.day_name[my_date.weekday()] == 'saturday' or 'sunday':
            result.append(key)

    print(result)


saturday_sunday()


def city_z():
    dictionary = {}
    for key, value in zip(city, pincode):
        if key in dictionary:
            if 'z' or 'Z' in key:
                dictionary[key].append(value)
        else:
            dictionary[key] = [value]
    print(dictionary)
    dictionary_2 = {}
    for key, value in zip(store, pincode_stores):
        if key in dictionary_2:
            dictionary_2[key].append(value)
        else:
            dictionary_2[key] = [value]
    print(dictionary_2)

    for key, value in dictionary.items():
        for key2, value2 in dictionary_2.items():
            if value == value2:
                dictionary[key] = key2
    print(dictionary)


city_z()


def no_of_stores_city():
    dictionary = {}
    for key, value in zip(city, pincode):
        if key in dictionary:
            dictionary[key].append(value)
        else:
            dictionary[key] = value
    print(dictionary)

    dic = Counter(pincode_stores)
    dict1 = dict(dic)
    print(dict1)
    output = []
    for key, value in dict1.items():
        for key2, value2 in dictionary.items():
            if key == value2:
                output.append(value)
    print(output)

    no_of_stores = {}

    for key, value in zip(city, output):
        if key not in no_of_stores:
            no_of_stores[key] = value
    print(no_of_stores)


no_of_stores_city()
