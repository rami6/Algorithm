"""
Problem description
 - https://leetcode.com/problems/binary-tree-inorder-traversal/

Result
 - Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Binary Tree Inorder Traversal.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            return self.helper([], root)

        return []

    def helper(self, result, head):
        if head.left:
            self.helper(result, head.left)

        result.append(head.val)

        if head.right:
            self.helper(result, head.right)

        return result
