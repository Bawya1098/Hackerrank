input_list = [7, 1, 3, 2, 4, 5, 6]

sorted_list = []


def swap(term1, term2):
    term1, term2 = term2, term1
    return term1, term2


length = len(input_list)
for index in range(0, length - 1, 2):
    if input_list[index] > input_list[index + 1]:
        value = swap(input_list[index], input_list[index + 1])
        sorted_list.append(value)

    elif input_list[index] < input_list[index + 1]:
        value = input_list[index], input_list[index + 1]
        sorted_list.append(value)

print(sorted_list)
