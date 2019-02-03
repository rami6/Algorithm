"""
Problem description
 - https://leetcode.com/problems/two-sum/

Result
 - Runtime: 36 ms, faster than 99.75% of Python3 online submissions for Two Sum.
 - Memory Usage: 7.9 MB, less than 31.08% of Python3 online submissions for Two Sum.
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        index_dict = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in index_dict:
                return [i, index_dict[complement]]

            if nums[i] not in index_dict:
                index_dict[nums[i]] = i
