'''
Tests sorting algorithms.
'''

import time
import argparse

from bubble import bubble_sort
from counting import counting_sort
from heap import heap_sort
from insertion import insertion_sort
from linear import linear_sort
from merge import merge_sort
from quick import quick_sort
from radix import radix_sort
from randquick import randomquick_sort
from selection import selection_sort
from shell import shell_sort
from tim import tim_sort


def test_sort(arr, sort_func, name):
    t0 = time.time()
    sorted_arr = sort_func(arr)
    t1 = time.time()
    time_taken = (t1 - t0) * 1000
    
    print(f"Sorted ({name}): {sorted_arr}")
    print(f"Time taken: {time_taken:.5f} ms")
    
if __name__ == "__main__":
    algos = {"bubble": bubble_sort,
             "counting": counting_sort,
             "heap": heap_sort,
             "insertion": insertion_sort,
             "linear": linear_sort,
             "merge": merge_sort,
             "quick": quick_sort,
             "radix": radix_sort,
             "randquick": randomquick_sort,
             "selection": selection_sort,
             "shell": shell_sort,
             "tim": tim_sort}
    
    parser = argparse.ArgumentParser(description="Test sorting algorithms.")
    parser.add_argument("-m", "--method", type=str, default="linear", help="Sorting method to use (default: linear sort)")
    parser.add_argument("-a", "--array", type=str, default="64 34 25 12 22 11 90", help="Array to sort (default: '64 34 25 12 22 11 90')")
    args = parser.parse_args()
    
    try:
        arr = list(map(int, args.array.split()))
    except ValueError:
        print("Invalid array input. Provide a space-separated list of integers (e.g., '5 3 8 2').")
        exit(1)
    
    try:
        if args.method in algos:
            print(f"Original array: {arr}\n")
            test_sort(arr, algos[args.method], args.method)
        else:
            print(f"Unknown sorting method: {args.method}")
            print("Available methods:", ", ".join(algos.keys()))
    except Exception as e:
        print(f"Error: {e}")