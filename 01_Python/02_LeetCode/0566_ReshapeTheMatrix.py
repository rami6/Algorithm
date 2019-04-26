"""
Problem description
 - https://leetcode.com/problems/reshape-the-matrix/

Result
 - Runtime: 84 ms, faster than 93.99% of Python online submissions for Reshape the Matrix.
 - Memory Usage: 11.8 MB, less than 95.89% of Python online submissions for Reshape the Matrix.
"""


class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) == 0 or len(nums) * len(nums[0]) != r * c:
            return nums

        result = [[] for i in range(r)]
        row = 0
        col_count = 0
        for num_list in nums:
            for num in num_list:
                result[row].append(num)
                col_count += 1
                if col_count > c - 1:
                    row += 1
                    col_count = 0

        return result
