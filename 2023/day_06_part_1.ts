import fs from 'fs';


const input: string[] = fs.readFileSync('input.txt', 'utf8').split('\n');
const raceDurations = input[0].split(':')[1].trim().split(/\s+/).map((el) => Number(el));
const records = input[1].split(':')[1].trim().split(/\s+/).map((el) => Number(el));

let ans = 1;
for (let i = 0; i < raceDurations.length; i++) {
  let waysToWinRace = 0;
  const raceDuration = raceDurations[i];
  const record = records[i];
  for (let hold = 1; hold < raceDuration; hold++) {
    const movementMs = raceDuration - hold;
    const dist = hold * movementMs;
    if (dist > record) {
      waysToWinRace += 1;
    }
  }
  ans *= waysToWinRace;
}
console.log(ans);