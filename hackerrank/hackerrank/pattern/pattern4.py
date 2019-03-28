maxLength = 5
for row in range(1, maxLength + 1):
    space = (maxLength - row)
    number_of_stars = row
    for col in range(0, space):
        print(" ", end='')
    for star in range(0, number_of_stars):
            print('* ', end='')

    print(' ')
