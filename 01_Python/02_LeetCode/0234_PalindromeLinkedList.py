"""
Problem description
 - https://leetcode.com/problems/palindrome-linked-list/

Result
 - Runtime: 72 ms, faster than 97.57% of Python online submissions for Palindrome Linked List.
 - Memory Usage: 30.6 MB, less than 5.28% of Python online submissions for Palindrome Linked List.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        node_vals = []
        while head:
            node_vals.append(head.val)
            head = head.next

        for i in range(len(node_vals) // 2):
            if node_vals[i] != node_vals[-1 - i]:
                return False

        return True


"""
2nd answer:

Result
 - Runtime: 72 ms, faster than 97.57% of Python online submissions for Palindrome Linked List.
 - Memory Usage: 29.9 MB, less than 6.84% of Python online submissions for Palindrome Linked List.
"""


class Solution_2(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:
            return True

        fast = head
        slow = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        if fast:
            slow = slow.next

        while slow:
            if slow.val != prev.val:
                return False

            slow = slow.next
            prev = prev.next

        return True
