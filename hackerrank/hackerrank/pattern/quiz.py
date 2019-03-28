string='string'
length = len(string)
if length < 2:
    print("EMPTY STRING")
elif length == 2:
    print(string * 2)
else:
    print(string[0:2] + string[-2:])


