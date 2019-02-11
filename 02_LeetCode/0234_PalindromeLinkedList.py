"""
Problem description
 - https://leetcode.com/problems/palindrome-linked-list/

Result
 - Runtime: 76 ms, faster than 76.88% of Python online submissions for Palindrome Linked List.
 - Memory Usage: 28 MB, less than 9.37% of Python online submissions for Palindrome Linked List.
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
        if not head or (head and not head.next):
            return True

        node_vals = [head.val]
        while head.next:
            node_vals.append(head.next.val)
            head = head.next

        for i in range(len(node_vals) // 2):
            if node_vals[i] != node_vals[-1 - i]:
                return False

        return True
