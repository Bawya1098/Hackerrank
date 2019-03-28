# arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
arr = [1, 4, 4, 4, 5, 3]


def migratoryBirds(arr):
    maxcount = 0
    maxcountElement = 0
    countmap = {}
    for index in range(0, len(arr)):
        key = arr[index]
        if key in countmap.keys():
            countmap[key] = countmap[key] + 1
        else:
            countmap[key] = 1
        currentElementCount = countmap[key]
        if currentElementCount > maxcount:
            maxcount = currentElementCount
            maxcountElement = key
        if currentElementCount == maxcount:
            if maxcountElement > key:
                maxcountElement = key
    return maxcountElement


if __name__ == '__main__':
    print(migratoryBirds(arr))
