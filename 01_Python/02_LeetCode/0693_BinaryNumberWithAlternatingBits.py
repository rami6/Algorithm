"""
Problem description
 - https://leetcode.com/problems/binary-number-with-alternating-bits/

Result
 - Runtime: 16 ms, faster than 100.00% of Python online submissions for Binary Number with Alternating Bits.
 - Memory Usage: 10.7 MB, less than 59.09% of Python online submissions for Binary Number with Alternating Bits.
"""


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        current_remain = n % 2
        n //= 2

        while n > 0:
            if current_remain == n % 2:
                return False
            current_remain = n % 2
            n //= 2

        return True
