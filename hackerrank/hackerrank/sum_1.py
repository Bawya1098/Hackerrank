string = input("enter the string")

list = string.split(",")
print(list)
result = {}
count = 1
for elements in range(0, len(list)):
    result[list[elements]] = count
    if list[elements] in result.keys():
        result[list[elements]] = +1

print(result)
