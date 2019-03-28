arr = [1, 2, 3, 4, 5]
list = []


def minimaxsum(arr):
    for num in range(0, len(arr)):
        value = arr.pop(0)
        result = sum(arr)
        list.append(result)
        arr.append(value)
    print(min(list), end=' ')
    print(max(list))


if __name__ == '__main__':
    minimaxsum(arr)
