# LEETCODE 131

# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

from typing import List
from functools import cache

class Solution:
    @cache
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return [[]]

        res = []
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            
            if prefix == ''.join(reversed(prefix)):
                suffix = self.partition(s[i:])
                for j in suffix:
                    res.append([prefix] + j)
        
        return res