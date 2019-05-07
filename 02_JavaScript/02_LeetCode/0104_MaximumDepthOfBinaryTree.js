/*
Problem description
  - https://leetcode.com/problems/maximum-depth-of-binary-tree/

Result
  - Runtime: 64 ms, faster than 100.00% of JavaScript online submissions for Maximum Depth of Binary Tree.
  - Memory Usage: 37.1 MB, less than 18.69% of JavaScript online submissions for Maximum Depth of Binary Tree.
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
 * @return {number}
 */
const maxDepth = function (root) {
  let max = 0;
  helper(root, 0);
  return max;

  function helper(curr, count) {
    if (!curr) {
      max = Math.max(max, count);
      return;
    }

    count++;
    helper(curr.left, count);
    helper(curr.right, count);
  }
};