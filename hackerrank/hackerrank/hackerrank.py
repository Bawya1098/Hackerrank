n = 5
list = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]
d = {}
for element in list:
    if element not in d:
        d[element] = 1
    else:
        d[element] += 1

print(d)
captain_room = min(d.values())

for key, value in d.items():
    if value == captain_room:
        print(key)
