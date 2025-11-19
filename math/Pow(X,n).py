'''
LEETCODE 50 (Medium)

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x^0 = 1
        if n == 0:
            return 1.0
        # x^1 = x
        elif n == 1:
            return x
        
        # x^-n = 1 / x^n
        if n < 0:
            x = 1 / x
            n = -1 * n
        
        
        half = self.myPow(x, n // 2)
        
        # x^n = x^(n/2) * x^(n/2) if n is even
        if n % 2 == 0:
            return half * half
        # x^n = x * x^((n-1)/2)) * x^((n-1)/2)) if n is odd
        else:
            return half * half * x