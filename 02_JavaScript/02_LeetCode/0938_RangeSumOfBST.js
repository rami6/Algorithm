/*
Problem description
  - https://leetcode.com/problems/range-sum-of-bst/

Result
  - Runtime: 160 ms, faster than 81.01% of JavaScript online submissions for Range Sum of BST.
  - Memory Usage: 70.8 MB, less than 15.38% of JavaScript online submissions for Range Sum of BST.
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
  return helper(root);

  function helper(curr) {
    if (!curr) {
      return 0;
    }

    let sum = 0;

    if (curr.val > L) {
      sum += helper(curr.left);
    }

    if (curr.val < R) {
      sum += helper(curr.right);
    }

    if (curr.val >= L && curr.val <= R) {
      sum += curr.val;
    }

    return sum;
  }
};