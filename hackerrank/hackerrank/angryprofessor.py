def angryProfessor(k, a):
    count = 0
    for index in range(0, len(a)):
        if a[index] <= 0:
            count += 1
    print(count)
    if count >= k:
        print('NO')
    else:
        print('YES')


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)
