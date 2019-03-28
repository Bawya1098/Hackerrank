def compareTriplets(a, b):
    count_Alice = 0
    count_Bob = 0
    for index in range(0, len(a)):
            if a[index] < b[index]:
                count_Bob += 1
            elif a[index] > b[index]:
                count_Alice += 1




    print(count_Alice, end=' ')
    print(count_Bob)


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)
