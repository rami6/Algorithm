/*
Problem description
  - https://leetcode.com/problems/number-of-islands/

Result
  - Runtime: 68 ms, faster than 99.43% of JavaScript online submissions for Number of Islands.
  - Memory Usage: 37.8 MB, less than 47.64% of JavaScript online submissions for Number of Islands.
*/


/**
 * @param {character[][]} grid
 * @return {number}
 */
const numIslands = function (grid) {
  if (grid.length === 0 || grid[0].length === 0) {
    return 0;
  }

  let res = 0;
  const rows = grid.length;
  const columns = grid[0].length;

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < columns; c++) {
      if (helper(r, c)) {
        res++;
      };
    }
  }
  return res;

  function helper(r, c) {
    if (r >= 0 && r < rows && grid[r][c] === "1") {
      grid[r][c] = "0";
      helper(r, c - 1);
      helper(r, c + 1);
      helper(r - 1, c);
      helper(r + 1, c);
      return true;
    }
    return false;
  }
};