"""
Problem description
 - https://leetcode.com/problems/search-in-a-binary-search-tree/

Result
 - Runtime: 72 ms, faster than 72.42% of Python online submissions for Search in a Binary Search Tree.
 - Memory Usage: 15 MB, less than 100.00% of Python online submissions for Search in a Binary Search Tree.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        result = None

        if root.val == val:
            return root

        if val < root.val and root.left:
            result = self.searchBST(root.left, val)
        elif val > root.val and root.right:
            result = self.searchBST(root.right, val)

        return result
