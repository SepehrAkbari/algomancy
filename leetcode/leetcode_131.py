# Palindrome Partitioning

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
            # checking if start to i is a palindrome
            prefix = s[:i]
            
            if prefix == ''.join(reversed(prefix)):
                # if it is, we partition the rest of the string
                suffix = self.partition(s[i:])
                for j in suffix:
                    # combining all the partitions
                    res.append([prefix] + j)
        
        return res