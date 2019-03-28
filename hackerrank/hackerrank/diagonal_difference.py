# import math
# import os
# import random
# import re
# import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    sum_1 = 0
    sum_2 = 0

    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                sum_1 += arr[i][j]

            if i == n - j - 1:
                sum_2 += arr[i][j]

    difference = sum_1 - sum_2
    return difference


if __name__ == '__main__':

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
