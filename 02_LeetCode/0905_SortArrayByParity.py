"""
Problem description
 - https://leetcode.com/problems/sort-array-by-parity/

Result
 - Runtime: 100 ms, faster than 20.59% of Python online submissions for Sort Array By Parity.
 - Memory Usage: 11.4 MB, less than 100.00% of Python online submissions for Sort Array By Parity.
"""


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        for i in range(len(A)):
            if A[i] % 2 == 0:
                A.insert(0, A.pop(i))

        return A
