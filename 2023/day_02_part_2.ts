import fs from 'fs';

const LOOKUP = {'red': 12, 'green': 13, 'blue': 14};

const arr: string[] = fs.readFileSync('input.txt', 'utf8').split('\n');

let rtn = 0; // add up the IDs of the games that would have been possible
for (const s of arr) {
  const maxes = {'red': 0, 'green': 0, 'blue': 0};
  const [gameStr, playsStr] = s.split(': ');
  const plays = playsStr.split('; '); // [ '3 blue, 4 red', ' 1 red, 2 green, 6 blue', ' 2 green' ]
  for (const play of plays) {
    const colors = play.split(', '); // [ '3 blue', '4 red' ]
    for (const color of colors) {
      const [amount, colorName] = color.split(' ');
      maxes[colorName as keyof typeof maxes] = Math.max(Number(amount), maxes[colorName as keyof typeof maxes]);
    }
  }
  const power = Object.values(maxes).reduce((acc, amount) => acc * amount, 1);
  rtn += power;
}
console.log(rtn);
