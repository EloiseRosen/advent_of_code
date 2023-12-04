import fs from 'fs';

const arr: string[] = fs.readFileSync('input.txt', 'utf8').split('\n');

let ans = 0;
for (const line of arr) {
  let score = 0;
  const [_, nums] = line.split(': ');
  const [winNumsStr, presentNumsStr] = nums.split(' | ');
  const winNums = winNumsStr.trim().split(/\s+/);
  const presentNums = presentNumsStr.trim().split(/\s+/);
  for (const presentNum of presentNums) {
    // The first match makes the card worth one point and each match after the first 
    // doubles the point value of that card.
    if (winNums.includes(presentNum)) {
      if (score === 0) {
        score = 1;
      } else {
        score *= 2;
      }
    }
  }
  ans += score;
}
console.log(ans);
