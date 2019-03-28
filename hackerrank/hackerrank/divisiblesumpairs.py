def divisibleSumPairs(n, k, ar):
    list = []
    count = 0
    for index in range(0, len(ar)):
        for j in range(index + 1, len(ar)):
            sum = ar[index] + ar[j]
            if sum % k == 0:
                if index < j:
                    list.append(sum)
                count += 1

    return count


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
    print(result)
