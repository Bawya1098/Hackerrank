string = input("Enter the string with %20")
if '%20' not in string:
    print('string does not contains %20')
else:
    result_string = string.replace('%20', '===')
    print(result_string)
