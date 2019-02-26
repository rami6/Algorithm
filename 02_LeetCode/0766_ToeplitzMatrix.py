"""
Problem description
 - https://leetcode.com/problems/toeplitz-matrix/

Result
 - Runtime: 24 ms, faster than 100.00% of Python online submissions for Toeplitz Matrix.
 - Memory Usage: 10.9 MB, less than 10.00% of Python online submissions for Toeplitz Matrix.
"""


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix) in [0, 1]:
            return True

        import copy

        seq = copy.copy(matrix[0])

        for row in matrix[1:]:
            seq.insert(0, row[0])

        len_h = len(matrix[0])
        i = 0
        for row in matrix[::-1]:
            if row != seq[i:i + len_h]:
                return False
            i += 1

        return True
