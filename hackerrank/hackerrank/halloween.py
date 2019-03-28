p = 20
d = 3
m = 6
s = 85
result = []
count=0
cost = [20, 17, 14, 11, 8, 6, 6, 6, 6, 6, 6]
sum = 0
for element in range(0, len(cost) - 1, 2):

    value = cost[element + 1]
    sum1 = value + cost[element]
    sum = sum1 + sum
    if sum < s:
        result.append(cost[element])
        result.append(value)
print(result)
for index in range(0, len(result)):
    count += 1
print(count)