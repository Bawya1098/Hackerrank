def nonDivisibleSubset(k, S):
    for index in range(0, len(S)):
        count = S[index] / k
        print(S[index],int(count))



if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)
