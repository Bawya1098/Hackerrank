def rotLeft(a, d):
    rep=d
    for index in range(0, rep):
        value = a.pop(0)
        a.append(value)
    return a


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
    print(result)
