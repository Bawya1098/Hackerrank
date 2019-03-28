def nonDivisibleSubset(k, S):
    result_array = set()

    for index in range(0, len(S) + 1):
        for second_index in range(index + 1, len(S)):
            sum = S[index] + S[second_index]

            if sum % k != 0 and int((sum / k) % 2) != 0:
                result_array.add(S[index])
                result_array.add(S[second_index])
        # print(result_array)
    count = len(result_array)
    return count


if __name__ == '__main__':
    nk = input().split()

n = int(nk[0])

k = int(nk[1])

S = list(map(int, input().rstrip().split()))

result = nonDivisibleSubset(k, S)
print(result)

for i in range(0, len(S)):
    for j in range(i + 1, len(S)):
        print(S[i], S[j], (S[i] + S[j]) % k)
