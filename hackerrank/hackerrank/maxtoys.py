def maximumToys(prices, k):
    new_list = []
    count = 0
    for index in range(0, len(prices)):
        if k > prices[index] in prices:
            new_list.append(prices[index])
            if sum(new_list) > k:
                for elements in range(0, len(new_list) - 1):
                    count += 1
                print(count)
            else:
                count += 1
    print(count)


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
