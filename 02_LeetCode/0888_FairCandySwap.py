"""
Problem description
 - https://leetcode.com/problems/fair-candy-swap/

Result
 - Runtime: 340 ms, faster than 25.52% of Python online submissions for Fair Candy Swap.
 - Memory Usage: 11.9 MB, less than 90.14% of Python online submissions for Fair Candy Swap.
"""


class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        dif = (sum(A) - sum(B)) / 2
        A_is_bigger = True
        big = A
        small = B

        if dif < 0:
            dif *= -1
            A_is_bigger = False
            big = B
            small = A

        big.sort()

        for i in range(len(big) - 1, -1, -1):
            if big[i] - dif in small:
                if A_is_bigger:
                    return [big[i], big[i] - dif]
                else:
                    return [big[i] - dif, big[i]]
