'''
Advantage Shuffle

You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

Return any permutation of nums1 that maximizes its advantage with respect to nums2.
'''

from typing import List

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