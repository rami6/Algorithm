"""
Problem description
 - https://leetcode.com/problems/maximum-depth-of-binary-tree/

Result
 - Runtime: 28 ms, faster than 100.00% of Python online submissions for Maximum Depth of Binary Tree.
 - Memory Usage: 14.5 MB, less than 5.14% of Python online submissions for Maximum Depth of Binary Tree.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    max_depth = 0

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def help(node, depth):
            if not node.left and not node.right:
                self.max_depth = max(self.max_depth, depth)

            if node.left:
                help(node.left, depth + 1)

            if node.right:
                help(node.right, depth + 1)

        help(root, 1)
        return self.max_depth
