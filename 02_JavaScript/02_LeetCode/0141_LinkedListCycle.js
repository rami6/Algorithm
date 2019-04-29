/*
Problem description
  - https: //leetcode.com/problems/linked-list-cycle/

Result
  - Runtime: 72 ms, faster than 76.71 % of JavaScript online submissions for Linked List Cycle.
  - Memory Usage: 37.7 MB, less than 13.30 % of JavaScript online submissions for Linked List Cycle.
*/

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
const hasCycle = function (head) {
  const nodeSet = new Set();
  while (head) {
    if (nodeSet.has(head)) {
      return true;
    }
    nodeSet.add(head);
    head = head.next;
  }
  return false;
};