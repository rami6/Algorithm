"""
Problem description
 - https://leetcode.com/problems/peak-index-in-a-mountain-array/

Result
 - Runtime: 20 ms, faster than 100.00% of Python online submissions for Peak Index in a Mountain Array.
 - Memory Usage: 11.4 MB, less than 0.85% of Python online submissions for Peak Index in a Mountain Array.
"""


class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                return i
