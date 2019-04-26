"""
Problem description
 - https://leetcode.com/problems/isomorphic-strings/

Result
 - Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Invert Binary Tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = root.right, root.left

            if root.left:
                self.invertTree(root.left)
            if root.right:
                self.invertTree(root.right)

        return root
