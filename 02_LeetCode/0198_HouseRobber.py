"""
Problem description
 - https://leetcode.com/problems/house-robber/

Result
 - Runtime: 24 ms, faster than 31.98% of Python online submissions for House Robber.
 - Memory Usage: 11.9 MB, less than 5.29% of Python online submissions for House Robber.
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev1_res = 0
        prev2_res = 0

        for num in nums:
            tmp = prev1_res
            prev1_res = max(prev2_res + num, prev1_res)
            prev2_res = tmp

        return prev1_res
