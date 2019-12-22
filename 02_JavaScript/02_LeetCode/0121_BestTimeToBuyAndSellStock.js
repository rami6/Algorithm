/*
Problem description
  - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Result
  - Runtime: 60 ms, faster than 72.02% of JavaScript online submissions for Best Time to Buy and Sell Stock.
  - Memory Usage: 35.6 MB, less than 37.04% of JavaScript online submissions for Best Time to Buy and Sell Stock.
*/

/**
 * @param {number[]} prices
 * @return {number}
 */
const maxProfit = function (prices) {
  if (prices.length < 2) {
    return 0;
  }

  let minPrice = prices[0];
  let maxDif = 0;

  for (let i = 1; i < prices.length; i++) {
    maxDif = Math.max(maxDif, prices[i] - minPrice);
    minPrice = Math.min(minPrice, prices[i]);
  }
  return maxDif;
};