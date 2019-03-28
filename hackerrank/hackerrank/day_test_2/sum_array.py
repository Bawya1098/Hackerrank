def list(list):
    result = set()
    for elements in range(0, len(list) - 1):
        for index in range(1, len(list)):
            sum = list[elements] + list[index]
            if sum == 10 and elements != index:
                result.add(list[elements])
                result.add((list[index]))

    print(result)


list([1, 3, 7, 4, 5, 6])
