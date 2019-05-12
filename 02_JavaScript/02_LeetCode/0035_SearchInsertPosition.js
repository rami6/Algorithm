/*
Problem description
  - https://leetcode.com/problems/search-insert-position/

Result
  - Runtime: 48 ms, faster than 99.60% of JavaScript online submissions for Search Insert Position.
  - Memory Usage: 33.8 MB, less than 67.20% of JavaScript online submissions for Search Insert Position.
*/


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
const searchInsert = function (nums, target) {
  return binSearch(0, nums.length - 1);

  function binSearch(start, end) {
    const mid = Math.floor((start + end) / 2);

    if (nums[mid] === target) {
      return mid;
    }

    if (start === end) {
      return (nums[start] > target) ? start : start + 1;
    }

    if (nums[mid] > target) {
      return binSearch(start, mid);
    }

    if (nums[mid] < target) {
      return binSearch(mid + 1, end);
    }
  }
};