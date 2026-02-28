'''
Quicksort.
'''

def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    pivot = arr[n // 2]
    left, middle, right = [], [], []
    
    for i in range(n):
        if arr[i] < pivot:
            left.append(arr[i])
        if arr[i] == pivot:
            middle.append(arr[i])
        if arr[i] > pivot:
            right.append(arr[i])
            
    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)
    
    return left_sorted + middle + right_sorted