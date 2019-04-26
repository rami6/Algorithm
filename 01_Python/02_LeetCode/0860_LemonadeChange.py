"""
Problem description
 - https://leetcode.com/problems/lemonade-change/

Result
 - Runtime: 44 ms, faster than 100.00% of Python3 online submissions for Lemonade Change.
"""


class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        bill_5 = 0
        bill_10 = 0

        for bill in bills:
            if bill == 5:
                bill_5 += 1
            elif bill == 10 and bill_5 > 0:
                bill_5 -= 1
                bill_10 += 1
            elif bill == 20:
                if bill_10 > 0 and bill_5 > 0:
                    bill_5 -= 1
                    bill_10 -= 1
                elif bill_5 > 2:
                    bill_5 -= 3
                else:
                    return False
            else:
                return False

        return True
