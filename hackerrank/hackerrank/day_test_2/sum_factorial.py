def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


value = str(factorial(7))
list = []
for index in range(0, len(value)):
    list.append(int(value[index]))

print(sum(list))


