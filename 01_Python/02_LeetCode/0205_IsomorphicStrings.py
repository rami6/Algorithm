"""
Problem description
 - https://leetcode.com/problems/isomorphic-strings/

Result
 - Runtime: 56 ms, faster than 98.72% of Python3 online submissions for Isomorphic Strings.
"""


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_dict = {}

        for s_char, t_char in zip(s, t):
            if s_char not in char_dict:
                if t_char not in char_dict.values():
                    char_dict[s_char] = t_char
                else:
                    return False
            elif char_dict[s_char] != t_char:
                return False

        return True
