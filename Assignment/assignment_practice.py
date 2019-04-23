import pandas as csv

stores = csv.read_csv('stores.csv', delimiter=',')
location = csv.read_csv('exercise_1_location.csv', delimiter=',')


def build_area_4000():
    output_1 = stores['store_name'][stores['build_area'] >= 4000]
    print(output_1)


build_area_4000()


def most_number_stores():
    pincode_stores = stores['pincode']
    pincode_location = location['pincode']
    country = location['country']
    store = stores['store_name']
    pincode_list = []
    length = length_comparison(pincode_location, pincode_stores)
    for c in country:
        if pincode_stores[:length - 1] == pincode_location[:length - 1]:
            pincode_list.append(c)
    country_stores = find_country_stores(pincode_list, country, store)
    print(pincode_list)
    print(country_stores)


def length_comparison(pincode_location, pincode_stores):
    length_location = len(pincode_location)
    length_stores = len(pincode_stores)
    if length_location > length_stores:
        length_location = pincode_location[:length_stores]
        return length_location
    elif length_location == length_stores:
        return length_stores
    else:
        length_stores = pincode_stores[:length_location]
        return length_stores


def find_country_stores(pincode_list, country, store):
    d = dict()
    for c in range(0, len(pincode_list) - 1):
        if country[c] not in d.keys():
            d[country[c]] = store[c]
        else:
            d[country[c]] = d[country[c]] + ',' + store[c]
    values = d.values()
    values_list = []
    for v in values:
        values_list.append(v)
    for v in range(0, len(values_list) - 1):
        cal = len(values_list[v])
        cal_1 = len(values_list[v + 1])
        if cal < cal_1:
            max = values_list[v + 1]
        else:
            max = values_list[v]
    print(max)
    for key, value in d.items():
        if max == value:
            return key


most_number_stores()


def city_contain_z():
    city = location['city']
    store = stores['store_name']
    city_list = []
    d = {}
    for names in city:
        if "z" in str(names):
            city_list.append(names)
    for c in range(0, len(city_list) - 1):
        if city_list[c] not in d.keys():
            d[city_list[c]] = store[c]
        else:
            d[city_list[c]] = d[city_list[c]] + ',' + str(store[c])

    values = d.values()
    values_list = []
    print(values)

city_contain_z()


def no_of_stores():
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


no_of_stores()


def sum_buildarea():
    date = stores['date_of_opening']
    build_area_ = stores['build_area']
    date_list = []
    build_area = []
    for d in date:
        date_list.append(d)
    # print(date_list)
    for b in build_area_:
        build_area.append(b)
    # print(build_area)
    total_sum = []
    for i in range(0, len(date_list)):
        if '2018' or '18' in date_list[i]:
            total_sum.append(build_area[i])
        break

    print(sum(total_sum))


sum_buildarea()


def sunday_saturday():
    date = stores['date_of_opening']
    store = stores['store_name']
    date_list = []
    for d in date:
        date_list.append(d)
    print(date_list)
    for i in date_list:
        date = i.split('/')
        print(date)


sunday_saturday()
