/* Weekly Contest
 * - https://leetcode.com/contest/weekly-contest-172/problems/delete-leaves-with-a-given-value/
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
 * @param {number} target
 * @return {TreeNode}
 */
const removeLeafNodes = function (root, target) {
  removeNode(null, root, false);
  return root.val === target && !root.left && !root.right ? null : root;

  function removeNode(prev, curr, isLeft) {
    if (curr.left) {
      curr = removeNode(curr, curr.left, true);
    }

    if (curr.right) {
      curr = removeNode(curr, curr.right, false);
    }

    if (curr.val === target && !curr.left && !curr.right && prev) {
      if (isLeft) {
        prev.left = null;
      } else {
        prev.right = null;
      }
    }

    return prev;
  }
};