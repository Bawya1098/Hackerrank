max_length = 9


for row in range(1, max_length + 1):
    star = row
    space_range = (2 * max_length) - 1
    space_alloc = max_length / 2

    no_space = space_range - star - 1
    spaces = int(no_space - space_alloc)
    for column in range(0, star):
        print(row, end='')
    for space in range(1, spaces):
        print("  ", end='')
    for element in range(1, space_range - no_space):
        print(row, end='')

    print('')
