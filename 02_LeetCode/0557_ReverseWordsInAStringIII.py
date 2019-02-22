"""
Problem description
 - https://leetcode.com/problems/reverse-words-in-a-string-iii/

Result
 - Runtime: 40 ms, faster than 50.33% of Python online submissions for Reverse Words in a String III.
 - Memory Usage: 12 MB, less than 17.46% of Python online submissions for Reverse Words in a String III.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        result = ''
        for word in words:
            result += word[::-1] + ' '

        return result[:-1]
