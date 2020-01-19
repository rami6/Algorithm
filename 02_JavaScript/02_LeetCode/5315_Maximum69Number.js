/* Weekly Contest
 * - https://leetcode.com/contest/weekly-contest-172/problems/maximum-69-number/
*/

/**
 * @param {number} num
 * @return {number}
 */
const maximum69Number = function (num) {
  const numStrArr = (num.toString()).split('');
  const firstSixIndex = numStrArr.findIndex(n => n === '6');
  if (firstSixIndex < 0) {
    return num;
  }

  numStrArr[firstSixIndex] = '9';
  return parseInt(numStrArr.join(''));
};