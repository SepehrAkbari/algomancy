'''
Radix sort.
'''

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        arr = count(arr, exp)
        exp *= 10
        
    return arr
        
def count(arr, exp):
    sorted_arr = [0] * len(arr)
    counts = [0] * 10
    
    for i in arr:
        digit = (i // exp) % 10
        counts[digit] += 1
        
    for j in range(1, 10):
        counts[j] += counts[j - 1]
        
    for k in reversed(arr):
        digit = (k // exp) % 10
        target_idx = counts[digit] - 1
        sorted_arr[target_idx] = k
        counts[digit] -= 1
    
    return sorted_arr