"""
Problem description
 - https://leetcode.com/problems/climbing-stairs/

Result
 - Runtime: 36 ms, faster than 43.96% of Python3 online submissions for Climbing Stairs.
"""


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import factorial

        steps_1 = n
        steps_2 = 0
        count = 1

        while steps_1 >= 2:
            steps_1 -= 2
            steps_2 += 1
            count += factorial((steps_1 + steps_2)) // (factorial(steps_1) * factorial(steps_2))

        return count
