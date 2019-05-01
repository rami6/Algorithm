/*
Problem description
  - https://leetcode.com/problems/kth-largest-element-in-a-stream/

Result
  - Runtime: 208 ms, faster than 67.11 % of JavaScript online submissions for Kth Largest Element in a Stream.
  - Memory Usage: 45.4 MB, less than 14.29 % of JavaScript online submissions for Kth Largest Element in a Stream.
*/


/**
 * @param {number} k
 * @param {number[]} nums
 */
const KthLargest = function (k, nums) {
  this.k = k;
  nums.sort(function (a, b) {
    return b - a;
  });
  this.nums = nums.slice(0, k);
};

/** 
 * @param {number} val
 * @return {number}
 */
KthLargest.prototype.add = function (val) {
  if (this.nums.length === 0 || this.nums.length < this.k && val <= this.nums[this.k - 2]) {
    this.nums.push(val);
  } else if (this.nums.length < this.k || val >= this.nums[this.k - 1]) {
    let i = 0;
    while (i < this.k) {
      if (val >= this.nums[i]) {
        this.nums.splice(i, 0, val);
        break;
      }
      i++;
    }
  }
  return this.nums[this.k - 1];
};

/** 
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */