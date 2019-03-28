list = [-25, -10, -7, -3, 2, 4, 8, 10]
pos_list = []
neg_list = []
print(sorted(list))
for element in list:
    if element > 0:
        pos_list.append(element)
    else:
        neg_list.append(element)

print("pos_list", pos_list)
print("neg_list", neg_list)

for index in range(0, len(neg_list)):
    for pos_index in range(0, len(pos_list)):
        for second_index in range(1, len(pos_list) - 1):
            sum = pos_list[pos_index] + pos_list[second_index]
            if sum == abs(neg_list[index]):
                result_list = []
                value = neg_list[index], pos_list[pos_index], pos_list[second_index]
                result_list.append(value)
                print(result_list, end='')
for index in range(0, len(pos_list)):
    for neg_index in range(0, len(neg_list)):
        for second_index in range(1, len(neg_list) - 1):
            sum = neg_list[neg_index] + neg_list[second_index]
            if abs(sum) == pos_list[index]:
                result_list = []
                value = pos_list[index], neg_list[neg_index], neg_list[second_index]
                result_list.append(value)
                print(result_list)
