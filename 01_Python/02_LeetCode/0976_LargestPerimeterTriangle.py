"""
Problem description
 - https://leetcode.com/problems/largest-perimeter-triangle/

Result
 - Runtime: 48 ms, faster than 100.00% of Python online submissions for Largest Perimeter Triangle.
 - Memory Usage: 11.7 MB, less than 20.45% of Python online submissions for Largest Perimeter Triangle.
"""


class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        for i in range(len(A) - 3, -1, -1):
            if A[i] + A[i + 1] > A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]

        return 0
