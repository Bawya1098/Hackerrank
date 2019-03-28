from collections import defaultdict

group_a = []
group_b = []

line = input()
line = line.split()
m = int(line[0])
n = int(line[1])
for number in range(0, m):
    line = input()
    group_a.append(line)
for number in range(0, n):
    line = input()
    group_b.append(line)

d = defaultdict(list)
for index in range(0, len(group_a)):
    key = group_a[index]
    d[key].append(index + 1)

for element in group_b:
    value = d[element]
    if len(value) == 0:
        print('-1', end='')
    else:
        for i in value:
            print(i, end=' ')
    print('')
