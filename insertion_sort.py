#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n,arr):
    # Write your code here
    if len(arr)>1:
        tmp = arr.pop()
        arr.append(arr[-1])

        for i in range(len(arr)-2, -1, -1):
            if (i+1) < len(arr):
                if tmp < arr[i] and i!=0:
                    arr[i+1] = arr[i]
                    if i == 0:
                        arr[i] = tmp
                    for j in arr:
                        print(j, end=" ")
                elif tmp<arr[i] and i==0:
                    arr[i+1] = arr[i]
                    for j in arr:
                        print(j, end=" ")
                    print(end="\n")
                    arr[i]=tmp
                    for j in arr:
                        print(j, end=" ")
                    break
                else: 
                    arr[i+1] = tmp
                    for j in arr:
                        print(j, end=" ")
                    break
            print(end="\n")
    else:
        print(arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
