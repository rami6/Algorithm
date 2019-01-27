"""
Problem description
 - https://leetcode.com/problems/binary-tree-paths/

Result
 - Runtime: 40 ms, faster than 97.80% of Python3 online submissions for Binary Tree Paths.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        try:
            return self.helper(root, str(root.val), [])
        except:
            return []

    def helper(self, root, path, paths):
        if root.left == None and root.right == None:
            paths.append(path)
            return paths

        if root.left:
            self.helper(root.left, f'{path}->{root.left.val}', paths)

        if root.right:
            self.helper(root.right, f'{path}->{root.right.val}', paths)

        return paths
