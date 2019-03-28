list = [2, 3, 4, 1, 5]
length = len(list)
sorted_list = sorted(list)

for index in range(0, length):
    if list[index] > list[index + 1]:
        temp = list[index]
        list[index] = list[index + 1]
        list[index + 1] = temp
        break
    else:
        continue

print(list)
