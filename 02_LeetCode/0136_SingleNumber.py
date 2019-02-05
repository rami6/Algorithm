"""
Problem description
 - https://leetcode.com/problems/single-number/

Result
 - Runtime: 40 ms, faster than 84.89% of Python3 online submissions for Single Number.
 - Memory Usage: 9 MB, less than 27.50% of Python3 online submissions for Single Number.
"""


class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                del num_dict[num]

        return list(num_dict)[0]
