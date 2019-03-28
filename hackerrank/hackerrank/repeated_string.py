def repeatedString(s, n):
    print(len(s))
    print(n)
    if len(s) % 2 == 0:
        for index in range(0, (n // 2)):
            print(s, end='')
    else:
        limit = len(s) / n
        for index in range(0, int(limit)):
            print(s, end='')


if __name__ == '__main__':
    s = 'aba'

    n = 10

    result = repeatedString(s, n)
