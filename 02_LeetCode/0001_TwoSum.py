"""
Problem description
 - https://leetcode.com/problems/two-sum/

Result
 - Runtime: 816 ms, faster than 40.95% of Python3 online submissions for Two Sum.
 - Memory Usage: 7.3 MB, less than 71.72% of Python3 online submissions for Two Sum.
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            complement = target - nums[i]
            try:
                return [i, nums[i + 1:].index(complement) + i + 1]
            except:
                pass
