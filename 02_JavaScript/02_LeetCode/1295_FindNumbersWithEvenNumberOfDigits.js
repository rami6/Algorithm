/*
Problem description
  - https://leetcode.com/contest/weekly-contest-168/problems/find-numbers-with-even-number-of-digits/

Result
  - Runtime: 56 ms, faster than 100.00% of JavaScript online submissions for Find Numbers with Even Number of Digits.
  - Memory Usage: 34.8 MB, less than 100.00% of JavaScript online submissions for Find Numbers with Even Number of Digits.
*/


/**
 * @param {number[]} nums
 * @return {number}
 */
const findNumbers = function (nums) {
  let count = 0;
  const log10 = Math.log(10);
  nums.map(num => {
    let numOfDigits = Math.floor(Math.log(num) / log10) + 1;
    if (numOfDigits % 2 === 0) {
      count++;
    }
  })
  return count;
};