maxLength = 5

height = int((maxLength + 1) / 2)
for row in range(1, height + 1):
    stars = (maxLength - 2 * (row - 1))
    for col in range(0, row - 1):
        print(" ", end='')
    for star in range(0, stars):
        print("*", end='')
    print("")
