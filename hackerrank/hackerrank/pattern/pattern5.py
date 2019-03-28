maxLength = 5
for row in range(1, maxLength + 1):
    space = row - 1
    no_stars = (maxLength - row) + 1
    for col in range(0, space):
        print(" ", end='')
    for stars in range(0, no_stars):
        print("* ", end='')
    print('')
