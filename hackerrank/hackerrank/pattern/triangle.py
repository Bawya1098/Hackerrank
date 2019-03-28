maxLength = 5
for row in range(1, maxLength + 1):
    # for stars in range(1, star_value + 1):
    #     print("* ", end="")

    space = row - 1
    star_value = maxLength - row
    for spaces in range(1, space + 1):
        print(" ", end="")
    for stars in range(1, star_value + 1):
        print("* ", end="")


    print(' ')
