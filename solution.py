#!/bin/python3

import sys


def duplicateArray(arr):
    duplicate = []

    for i in range(0, len(arr)):
        duplicate.append(arr[i])

    return duplicate


arr = list(map(int, input().strip().split(' ')))

minimum = min(arr)
maximum = max(arr)

maximalSum = -9223372036854775808
minimalSum = 9223372036854775807

for i in range(0, len(arr)):
    sum = 0
    auxArr = duplicateArray(arr)
    auxArr.remove(auxArr[i])
    for num in auxArr:
        sum = sum + num

    if (sum > maximalSum):
        maximalSum = sum
    if (sum < minimalSum):
        minimalSum = sum

print(minimalSum, maximalSum)
