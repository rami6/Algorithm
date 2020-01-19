/* Weekly Contest
 * - https://leetcode.com/contest/weekly-contest-172/problems/print-words-vertically/
 */

/**
 * @param {string} s
 * @return {string[]}
 */
const printVertically = function (s) {
  const resArr = [];
  const words = s.split(' ');
  const longestWordLength = Math.max(...words.map(w => w.length));

  for (let i = 0; i < longestWordLength; i++) {
    if (words[0][i]) {
      resArr.push(words[0][i]);
    } else {
      resArr.push(' ');
    }
  }

  for (let i = 0; i < longestWordLength; i++) {
    for (const word of words.slice(1)) {
      if (word[i]) {
        resArr[i] += word[i];
      } else {
        resArr[i] += ' ';
      }
    }
  }

  return resArr.map(s => s.trimEnd());
};