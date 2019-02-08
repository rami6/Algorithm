"""
Problem description
 - https://leetcode.com/problems/intersection-of-two-linked-lists/

Result
 - Runtime: 200 ms, faster than 86.64% of Python online submissions for Intersection of Two Linked Lists.
 - Memory Usage: 65.9 MB, less than 2.88% of Python online submissions for Intersection of Two Linked Lists.
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

        i = 0
        while True:
            i += 1
            if headA.next:
                list_A.append(headA.next)
                headA = headA.next

            if headB.next:
                dict_B[headB.next] = i
                headB = headB.next

            if not headA.next and not headB.next:
                break

        for node in list_A:
            if node in dict_B:
                return node

        return None
