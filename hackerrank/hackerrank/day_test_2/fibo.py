fibo = [1, 1]
n = 4
for i in range(n - 1):
    fibo.append(fibo[i] + fibo[i + 1])

print(fibo)
result_list = []
for elements in range(0, len(fibo)):
    fibo[elements] = fibo[elements] ** 3
    result_list.append(fibo[elements])
print(result_list)
print(sum(result_list))
