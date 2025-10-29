'''
LEETCODE 870 (Medium)

You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

Return any permutation of nums1 that maximizes its advantage with respect to nums2.
'''

from typing import List

# step by step explanation:
# 1. Sort nums1 to facilitate finding the smallest number greater than a given number.
# 2. For each number in nums2, use binary search to find the smallest number in nums1 that is greater than that number.
# 3. If such a number is found, assign it to the result for that index and remove it from nums1.
# 4. If no such number is found, assign the smallest number in nums1 to that index and remove it from nums1.
# 5. Return the result array.
def main(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()

    result = [-1] * len(nums2)

    for i, num in enumerate(nums2):
        left, right = 0, len(nums1) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums1[mid] > num:
                right = mid - 1
            else:
                left = mid + 1

        if left < len(nums1):
            result[i] = nums1[left]
            nums1.pop(left)
        else:
            result[i] = nums1[0]
            nums1.pop(0) 

    return result