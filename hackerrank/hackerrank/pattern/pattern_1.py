maxLength = 15
for row in range(0, maxLength):
    for col in range(row, maxLength - 1):
        print("*", end='')
    print(" ")
