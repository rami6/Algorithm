"""
Problem description
 - https://leetcode.com/problems/two-sum/

Result
 - Runtime: 4824 ms, faster than 19.01% of Python3 online submissions for Two Sum.
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
