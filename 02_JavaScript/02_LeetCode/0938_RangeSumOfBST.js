/*
Problem description
  - https://leetcode.com/problems/range-sum-of-bst/

Result
  - Runtime: 176 ms, faster than 98.64 % of JavaScript online submissions for Range Sum of BST.
  - Memory Usage: 67.2 MB, less than 23.20 % of JavaScript online submissions for Range Sum of BST.
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
 * @param {number} L
 * @param {number} R
 * @return {number}
 */
const rangeSumBST = function (root, L, R) {
  if (root) {
    return helper(root, 0);
  }
  return 0;

  function helper(curr, sum) {
    if (!curr) {
      return sum;
    }

    if (curr.val >= L && curr.val <= R) {
      sum += curr.val;
    }

    if (curr.val > L) {
      sum = helper(curr.left, sum);
    }

    if (curr.val < R) {
      sum = helper(curr.right, sum);
    }

    return sum;
  }
};