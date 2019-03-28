user_input = str(input("Enter the string:"))
input = user_input.lower()
word = input.split(',')
list = []
for elements in word:
    list.append(elements)

result = sorted(list)
print(result)
