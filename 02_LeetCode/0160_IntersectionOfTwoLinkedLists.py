"""
Problem description
 - https://leetcode.com/problems/intersection-of-two-linked-lists/

Result
 - Runtime: 620 ms, faster than 1.24% of Python online submissions for Intersection of Two Linked Lists.
 - Memory Usage: 62.7 MB, less than 15.81% of Python online submissions for Intersection of Two Linked Lists.
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

        stack_A = [headA]
        stack_B = [headB]

        while headA.next:
            stack_A.insert(0, headA.next)
            headA = headA.next

        while headB.next:
            stack_B.insert(0, headB.next)
            headB = headB.next

        i = 0
        while i < min(len(stack_A), len(stack_B)) and stack_A[i] == stack_B[i]:
            i += 1

        if i == 0:
            return None
        else:
            return stack_A[i - 1]
