"""
Problem description
 - https://leetcode.com/problems/univalued-binary-tree/

Result
 - Runtime: 20 ms, faster than 100.00% of Python online submissions for Univalued Binary Tree.
 - Memory Usage: 7 MB, less than 65.96% of Python online submissions for Univalued Binary Tree.
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
                return False

            if isUnival and head.left:
                isUnival = helper(first_val, head.left, isUnival)

            if isUnival and head.right:
                isUnival = helper(first_val, head.right, isUnival)

            return isUnival

        return helper(root.val, root, True)
