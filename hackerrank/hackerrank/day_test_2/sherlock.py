from collections import Counter
s = 'aabbccdde'
dict = {}

for element in s:
    if element not in dict:
        dict[element] = 1
    else:
        dict[element] += 1

print(dict)
values = dict.values()
list = []
for val in values:
    list.append(val)
print(list)
print(Counter(list))
