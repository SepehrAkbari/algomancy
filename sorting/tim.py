'''
Tim sort.
'''

def tim_sort(arr, min_merge=32):
    n = len(arr)
    
    for i in range(0, n, min_merge):
        left_idx = i
        right_idx = min(i + min_merge - 1, n - 1)
        _insertion_sort(arr, left_idx, right_idx)
        
    size = min_merge
    while size < n:
        for left_idx in range(0, n, 2 * size):
            mid_idx = left_idx + size - 1
            right_idx = min((left_idx + 2 * size - 1), (n - 1))
            _merge(arr, left_idx, mid_idx, right_idx)
            
        size *= 2
    
    return arr

def _insertion_sort(arr, left_idx, right_idx):
    for i in range(left_idx + 1, right_idx + 1):
        key = arr[i]
        j = i
        
        while arr[j - 1] > key and j > left_idx:
            arr[j] = arr[j - 1]
            j -= 1
        
        arr[j] = key
        
    return arr

def _merge(arr, left_idx, mid_idx, right_idx):
    left = arr[left_idx:mid_idx + 1]
    right = arr[mid_idx + 1:right_idx + 1]
    
    i = j = 0
    k = left_idx
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        
    return arr