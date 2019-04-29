/*
Problem description
  - https://leetcode.com/problems/valid-parentheses/

Result
  - Runtime: 56 ms, faster than 100.00 % of JavaScript online submissions for Valid Parentheses.
  - Memory Usage: 33.9 MB, less than 56.75 % of JavaScript online submissions for Valid Parentheses.
*/


/**
 * @param {string} s
 * @return {boolean}
 */
const isValid = function (s) {
  const parenthesisDict = {
    '(': ')',
    '{': '}',
    '[': ']'
  };
  const stack = [];

  for (const c of s) {
    if (c in parenthesisDict) {
      stack.push(c);
    } else if (stack.length > 0 && parenthesisDict[stack[stack.length - 1]] === c) {
      stack.pop();
    } else {
      return false;
    }
  }

  if (stack.length === 0) {
    return true;
  }

  return false;
};