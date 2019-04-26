"""
Problem description
 - https://leetcode.com/problems/reverse-words-in-a-string-iii/

Result
 - Runtime: 24 ms, faster than 99.93% of Python online submissions for Reverse Words in a String III.
 - Memory Usage: 12.2 MB, less than 6.35% of Python online submissions for Reverse Words in a String III.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        reversed_words = s.split()[::-1]
        return ' '.join(reversed_words)
