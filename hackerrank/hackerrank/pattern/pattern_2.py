maxLength = 5

for row in range(0, maxLength + 1):
    for col in range(0, row):
        print(' ', end='')
    for star in range(0, maxLength - row):
        print("*", end='')
    print('')
