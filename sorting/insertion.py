'''
Insertion sort.
'''

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        
        while arr[i - 1] > key and i > 0:
            arr[i] = arr[i - 1]
            i -= 1
            
        arr[i] = key
        
    return arr