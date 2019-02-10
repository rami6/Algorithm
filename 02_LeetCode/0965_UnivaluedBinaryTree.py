"""
Problem description
 - https://leetcode.com/problems/univalued-binary-tree/

Result
 - Runtime: 20 ms, faster than 100.00% of Python online submissions for Univalued Binary Tree.
 - Memory Usage: 7.1 MB, less than 10.01% of Python online submissions for Univalued Binary Tree.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def helper(first_val, head, isUnival):
            if head.val != first_val:
                isUnival = False

            if head.left and isUnival:
                isUnival = helper(first_val, head.left, isUnival)

            if head.right and isUnival:
                isUnival = helper(first_val, head.right, isUnival)

            return isUnival

        return helper(root.val, root, True)
