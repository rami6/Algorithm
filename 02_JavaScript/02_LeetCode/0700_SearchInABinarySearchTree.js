/*
Problem description
  - https://leetcode.com/problems/search-in-a-binary-search-tree/

Result
  - Runtime: 68 ms, faster than 98.30% of JavaScript online submissions for Search in a Binary Search Tree.
  - Memory Usage: 41.8 MB, less than 56.25% of JavaScript online submissions for Search in a Binary Search Tree.
*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} val
 * @return {TreeNode}
 */
const searchBST = function (root, val) {
  if (!root) {
    return null;
  }

  if (root.val === val) {
    return root;
  }

  if (root.val > val) {
    return searchBST(root.left, val)
  }

  if (root.val < val) {
    return searchBST(root.right, val);
  }

  return null;
};