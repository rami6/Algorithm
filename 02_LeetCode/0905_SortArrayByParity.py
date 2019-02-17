"""
Problem description
 - https://leetcode.com/problems/sort-array-by-parity/

Result
 - Runtime: 56 ms, faster than 99.82% of Python online submissions for Sort Array By Parity.
 - Memory Usage: 11.5 MB, less than 100.00% of Python online submissions for Sort Array By Parity.
"""


class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []

        for num in A:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        return even + odd
