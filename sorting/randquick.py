'''
Randomized Quicksort.
'''

import random


def randomquick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    pivot = arr[random.choice(range(n))]
    left, middle, right = [], [], []
    
    for i in range(n):
        if arr[i] < pivot:
            left.append(arr[i])
        if arr[i] == pivot:
            middle.append(arr[i])
        if arr[i] > pivot:
            right.append(arr[i])
            
    left_sorted = randomquick_sort(left)
    right_sorted = randomquick_sort(right)
    
    return left_sorted + middle + right_sorted