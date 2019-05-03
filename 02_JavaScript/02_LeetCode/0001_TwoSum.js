/*
Problem description
  - https://leetcode.com/problems/two-sum/

Result
  - Runtime: 60 ms, faster than 94.01 % of JavaScript online submissions for Two Sum.
  - Memory Usage: 35.4 MB, less than 26.07 % of JavaScript online submissions for Two Sum.
*/


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = function (nums, target) {
  let i = 0;
  const numsDict = {};
  while (i < nums.length) {
    const complement = target - nums[i];
    if (complement in numsDict) {
      return [i, numsDict[complement]];
    }

    if (!(nums[i] in numsDict)) {
      numsDict[nums[i]] = i;
    }

    i++;
  }
};