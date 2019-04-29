/*
Problem description
  - https: //leetcode.com/problems/linked-list-cycle/

Result
  - Runtime: 72 ms, faster than 76.71 % of JavaScript online submissions for Linked List Cycle.
  - Memory Usage: 37.6 MB, less than 20.23 % of JavaScript online submissions for Linked List Cycle.
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
  if (!head || !head.next || !head.next.next) {
    return false;
  }

  let nodes = new Set([head, head.next]);
  while (head.next.next) {
    if (nodes.has(head.next.next)) {
      return true;
    }
    nodes.add(head.next.next);
    head = head.next;
  }
  return false;
};