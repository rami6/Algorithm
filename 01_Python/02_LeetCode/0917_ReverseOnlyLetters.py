"""
Problem description
 - https://leetcode.com/problems/reverse-only-letters/

Result
 - Runtime: 20 ms, faster than 84.78% of Python online submissions for Reverse Only Letters.
 - Memory Usage: 10.7 MB, less than 77.55% of Python online submissions for Reverse Only Letters.
"""


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        f_ptr = 0
        b_ptr = len(S) - 1
        chr_asciis = range(65, 91) + range(97, 123)
        result = ''

        while f_ptr < len(S):
            if ord(S[f_ptr]) in chr_asciis and ord(S[b_ptr]) in chr_asciis:
                result += S[b_ptr]
                f_ptr += 1
                b_ptr -= 1
            elif ord(S[f_ptr]) in chr_asciis:
                b_ptr -= 1
            elif ord(S[b_ptr]) in chr_asciis:
                result += S[f_ptr]
                f_ptr += 1
            else:
                result += S[f_ptr]
                f_ptr += 1
                b_ptr -= 1

        return result
