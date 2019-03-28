n = 5
r_q = 4
c_q = 3
obstacles = [[5, 5], [4, 2], [2, 3]]


def is_obstacle_position(row, col, obstacles):
    position = [row, col]
    return position in obstacles


def queensAttack(n, k, r_q, c_q, obstacles):
    count = 0
    for row in range(r_q + 1, n + 1, 1):
        if is_obstacle_position(row, c_q, obstacles):
            break
        else:
            count += 1
    print(count)

    for row_down in range(r_q - 1, 0, -1):
        if is_obstacle_position(row_down, c_q, obstacles):
            break
        else:
            count += 1
    print(count)

    for column_left in range(c_q - 1, 0, -1):
        if is_obstacle_position(r_q, column_left, obstacles):
            break
        else:
            count += 1

    print(count)
    for column_right in range(c_q + 1, n + 1):
        if is_obstacle_position(r_q, column_right, obstacles):
            break
        else:
            count += 1
    print(count)

    row = r_q + 1
    col = c_q - 1
    while row <= n and col >= 1:
        if is_obstacle_position(row, col, obstacles):
            break
        else:
            row += 1
            col -= 1
            count += 1
    print(count)

    row = r_q + 1
    col = c_q + 1
    while row <= n and col <= n:
        if is_obstacle_position(row, col, obstacles):
            break
        else:
            row += 1
            col += 1
            count += 1
    print(count)

    row = r_q - 1
    col = c_q - 1
    while row >= 1 and col >= 1:
        if is_obstacle_position(row, col, obstacles):
            break
        else:
            row -= 1
            col -= 1
            count += 1
    print(count)

    row = r_q - 1
    col = c_q + 1
    while row >= 1 and col <= n:
        if is_obstacle_position(row, col, obstacles):
            break
        else:
            row -= 1
            col += 1
            count += 1
    return count


print(queensAttack(n, 3, r_q, c_q, obstacles))
