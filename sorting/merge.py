'''
Merge sort.
'''


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    return merger(merge_sort(left), merge_sort(right))

def merger(left, right):
    sorted_arr = []
    l, r = 0, 0
    
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted_arr.append(left[l])
            l += 1
        else:
            sorted_arr.append(right[r])
            r += 1
    
    for i in range(l, len(left)):
        sorted_arr.append(left[i])
    for i in range(r, len(right)):
        sorted_arr.append(right[i])
    
    return sorted_arr