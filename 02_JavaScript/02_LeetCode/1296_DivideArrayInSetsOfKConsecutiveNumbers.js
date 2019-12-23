/*
Problem description
  - https://leetcode.com/contest/weekly-contest-168/problems/divide-array-in-sets-of-k-consecutive-numbers/

Result
  - Runtime: 216 ms, faster than 100.00% of JavaScript online submissions for Divide Array in Sets of K Consecutive Numbers.
  - Memory Usage: 64.7 MB, less than 100.00% of JavaScript online submissions for Divide Array in Sets of K Consecutive Numbers.
*/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */

const isPossibleDivide = function (nums, k) {
  if (nums.length % k !== 0) {
    return false;
  }

  const numsCountByNum = nums.reduce((acc, num) => {
    if (acc[num]) {
      acc[num]++;
    } else {
      acc[num] = 1;
    }
    return acc;
  }, {});

  const uniqueNums = Array.from(new Set(nums)).sort((a, b) => a - b);
  const numOfUniqueNums = uniqueNums.length;
  let currentMinIndexInUniqueNums = 0;

  let remainingSets = nums.length / k;

  while (remainingSets > 0) {
    for (let i = uniqueNums[currentMinIndexInUniqueNums]; i < uniqueNums[currentMinIndexInUniqueNums] + k; i++) {
      if (!numsCountByNum[i]) {
        return false;
      }
      numsCountByNum[i]--;
    }

    remainingSets--;

    while (!numsCountByNum[uniqueNums[currentMinIndexInUniqueNums]] && currentMinIndexInUniqueNums < numOfUniqueNums - k + 1) {
      currentMinIndexInUniqueNums++;
    }
  }

  return true;
};
