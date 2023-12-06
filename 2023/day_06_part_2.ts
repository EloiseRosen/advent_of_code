import fs from 'fs';


const input: string[] = fs.readFileSync('input.txt', 'utf8').split('\n');
const raceDuration = Number(input[0].split(':')[1].replace(/\s/g, ''));
const record = Number(input[1].split(':')[1].replace(/\s/g, ''));

let waysToWinRace = 0;
for (let hold = 1; hold < raceDuration; hold++) {
  const movementMs = raceDuration - hold;
  const dist = hold * movementMs;
  if (dist > record) {
    waysToWinRace += 1;
  }
}
console.log(waysToWinRace);
