import math

s = "chillout"


def encryption(s):
    s = s.replace(" ", "")
    length = len(s)
    sqrt_length = math.sqrt(length)
    no_rows = math.floor(sqrt_length)
    no_columns = math.ceil(sqrt_length)
    condition = no_columns * no_rows
    if condition < length:
        no_rows += 1   
    grid = []
    for rowNo in range(0, no_rows):
        starting_index = (rowNo * no_columns)
        ending_index = ((rowNo + 1) * no_columns)
        grid.append(s[starting_index:ending_index])
    print(grid)
    for column in range(0, no_columns):
        for row in range(0, no_rows):
            string = grid[row]
            if column < len(string):
                print(string[column], end='')

        print(' ', end='')


if __name__ == '__main__':
    encryption(s)
