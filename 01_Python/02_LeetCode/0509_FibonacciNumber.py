"""
Problem description
 - https://leetcode.com/problems/fibonacci-number/

Result
 - Runtime: 16 ms, faster than 100.00% of Python online submissions for Fibonacci Number.
 - Memory Usage: 10.9 MB, less than 5.25% of Python online submissions for Fibonacci Number.
"""


class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        elif N == 1:
            return 1

        pre_2 = 0
        pre_1 = 1

        for i in range(2, N + 1):
            temp = pre_1
            pre_1 += pre_2
            pre_2 = temp

        return pre_1
