"""
Problem description
 - https://leetcode.com/problems/intersection-of-two-linked-lists/

Result
 - Runtime: 196 ms, faster than 93.20% of Python online submissions for Intersection of Two Linked Lists.
 - Memory Usage: 66.2 MB, less than 1.32% of Python online submissions for Intersection of Two Linked Lists.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        list_A = [headA]
        dict_B = {headB: 0}

        while headA.next:
            list_A.append(headA.next)
            headA = headA.next

        while headB.next:
            dict_B[headB.next] = 0
            headB = headB.next

        for node in list_A:
            if node in dict_B:
                return node

        return None
