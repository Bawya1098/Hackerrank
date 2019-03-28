list = [0, 0, 0, 0, 1, 0]

count_list = []

for index in range(0, len(list)):
    value_ = list[index]
    value = list.count(value_)
    count_list.append(value)

count = max(count_list) - 1

print(count)
