"""
Problem description
 - https://leetcode.com/problems/verifying-an-alien-dictionary/

Result
 - Runtime: 16 ms, faster than 100.00% of Python online submissions for Verifying an Alien Dictionary.
 - Memory Usage: 10.7 MB, less than 71.62% of Python online submissions for Verifying an Alien Dictionary.
"""


class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_dict = {}
        i = 0
        for c in order:
            order_dict[c] = i
            i += 1

        pre = words[0]
        for word in words[1:]:
            for j in range(min(len(pre), len(word))):
                if order_dict[pre[j]] < order_dict[word[j]]:
                    break
                if order_dict[pre[j]] > order_dict[word[j]]:
                    return False
                if len(pre) > len(word) and j == min(len(pre), len(word)) - 1:
                    return False
            pre = word

        return True
