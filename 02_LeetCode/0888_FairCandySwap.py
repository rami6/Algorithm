"""
Problem description
 - https://leetcode.com/problems/fair-candy-swap/

Result
 - Runtime: 40 ms, faster than 100.00% of Python online submissions for Fair Candy Swap.
 - Memory Usage: 12.8 MB, less than 26.76% of Python online submissions for Fair Candy Swap.
"""


class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        dif = (sum(B) - sum(A)) / 2
        set_B = set(B)

        for num in A:
            if num + dif in set_B:
                return [num, num + dif]
