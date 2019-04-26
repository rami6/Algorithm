"""
Problem description
 - https://leetcode.com/problems/binary-tree-level-order-traversal/

Result
 - Runtime: 40 ms, faster than 95.16% of Python3 online submissions for Binary Tree Level Order Traversal.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root:
            return self.helper(root, [[root.val]], 1)
        else:
            return []

    def helper(self, head, result, lv):
        if not head.left and not head.right:
            return result

        if len(result) < lv + 1:
            result.append([])

        if head.left:
            result[lv].append(head.left.val)
            self.helper(head.left, result, lv + 1)
        if head.right:
            result[lv].append(head.right.val)
            self.helper(head.right, result, lv + 1)

        return result
