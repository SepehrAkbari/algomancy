'''
Shell sort.
'''

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i
            
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
                
            arr[j] = key
            
        gap //= 2
    
    return arr