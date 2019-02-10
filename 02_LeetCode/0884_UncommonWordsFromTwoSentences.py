"""
Problem description
 - https://leetcode.com/problems/uncommon-words-from-two-sentences/

Result
 - Runtime: 20 ms, faster than 100.00% of Python online submissions for Uncommon Words from Two Sentences.
 - Memory Usage: 7 MB, less than 93.29% of Python online submissions for Uncommon Words from Two Sentences.
"""


class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        import collections
        A_dict = collections.Counter(A.split())
        B_dict = collections.Counter(B.split())
        result = []

        for word in A_dict:
            if word not in B_dict and A_dict[word] == 1:
                result.append(word)

        for word in B_dict:
            if word not in A_dict and B_dict[word] == 1:
                result.append(word)

        return result
