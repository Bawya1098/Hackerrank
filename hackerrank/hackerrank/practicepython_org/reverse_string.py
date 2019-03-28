print("Enter a long string:")
user_input = input()
splited_input = user_input.split(" ")
result_list = splited_input[::-1]
for index in range(0, len(result_list)):
    print(result_list[index], end=' ')
