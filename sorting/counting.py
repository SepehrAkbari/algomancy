'''
Counting sort.
'''

def counting_sort(arr):
    counts = [0] * (max(arr) + 1)
    
    for i in arr:
        counts[i] += 1
    
    sorted_arr = []
    for i in range(len(counts)):
        for _ in range(counts[i]):
            sorted_arr.append(i)
    
    return sorted_arr