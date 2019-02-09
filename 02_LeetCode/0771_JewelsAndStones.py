"""
Problem description
 - https://leetcode.com/problems/jewels-and-stones/

Result
 - Runtime: 40 ms, faster than 86.28% of Python3 online submissions for Jewels and Stones.
 - Memory Usage: 6.5 MB, less than 89.39% of Python3 online submissions for Jewels and Stones.
"""


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        import collections
        counter = collections.Counter(S)
        result = 0

        for jChar in J:
            result += counter[jChar]

        return result
