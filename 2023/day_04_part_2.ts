import fs from 'fs';

const arr: string[] = fs.readFileSync('input.txt', 'utf8').split('\n');

// populate initial card count object with count of 1 for each card identfier
const cardCount: Record<string, number> = {}; // {card identifier: count of this card}
for (let n = 1; n < arr.length + 1; n++) {
  cardCount[n] = 1;
}

let ans = 0;
let currCard = 1;
for (const line of arr) {
  const [_, nums] = line.split(': ');
  const [winNumsStr, presentNumsStr] = nums.split(' | ');
  const winNums = winNumsStr.trim().split(/\s+/);
  const presentNums = presentNumsStr.trim().split(/\s+/);

  // count up number of matches
  let numMatches = 0;
  for (const presentNum of presentNums) {
    if (winNums.includes(presentNum)) {
      numMatches += 1;
    }
  }

  // update card counts accordingly: win copies of the scratchcards below the 
  // winning card equal to the number of matches
  for (let addAmount = 1; addAmount <= numMatches; addAmount++) {
    cardCount[currCard+addAmount] += cardCount[currCard];
  }

  ans += cardCount[currCard];
  currCard++;
}
console.log(ans);
