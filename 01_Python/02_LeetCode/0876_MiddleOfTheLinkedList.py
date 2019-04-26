"""
Problem description
 - https://leetcode.com/problems/middle-of-the-linked-list/

Result
 - Runtime: 20 ms, faster than 96.59% of Python online submissions for Middle of the Linked List.
 - Memory Usage: 10.9 MB, less than 100.00% of Python online submissions for Middle of the Linked List.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if fast.next:
            slow = slow.next

        return slow
