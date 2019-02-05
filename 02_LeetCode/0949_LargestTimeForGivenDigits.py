"""
Problem description
 - https://leetcode.com/problems/largest-time-for-given-digits/

Result
 - Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Largest Time for Given Digits.
 - Memory Usage: 6.5 MB, less than 40.00% of Python3 online submissions for Largest Time for Given Digits.

"""
import itertools


class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """

        result = ''
        largest = -1
        for num1, num2, num3, num4 in itertools.permutations(A):
            hh = num1 * 10 + num2
            mm = num3 * 10 + num4
            total_minutes = hh * 60 + mm
            if hh < 24 and mm < 60 and largest < total_minutes:
                largest = total_minutes
                if hh < 10:
                    hh = f'0{hh}'
                if mm < 10:
                    mm = f'0{mm}'
                result = f'{hh}:{mm}'

        return result
