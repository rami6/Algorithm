/*
Problem description
  - https: //leetcode.com/problems/same-tree/

Result
  - Runtime: 56 ms, faster than 54.15 % of JavaScript online submissions for Same Tree.
  - Memory Usage: 33.7 MB, less than 93.33 % of JavaScript online submissions for Same Tree.
*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
const isSameTree = function (p, q) {
  if (!p || !q) {
    return p === q;
  }

  if (p.val !== q.val) {
    return false;
  }

  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};