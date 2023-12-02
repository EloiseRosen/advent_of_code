import fs from 'fs';

const LOOKUP = {'red': 12, 'green': 13, 'blue': 14};

const arr: string[] = fs.readFileSync('input.txt', 'utf8').split('\n');

let rtn = 0; // add up the IDs of the games that would have been possible
for (const s of arr) {
  let valid = true;
  const [gameStr, playsStr] = s.split(': ');
  const game = Number(gameStr.slice(5,));
  const plays = playsStr.split('; '); // [ '3 blue, 4 red', ' 1 red, 2 green, 6 blue', ' 2 green' ]
  for (const play of plays) {
    const colors = play.split(', '); // [ '3 blue', '4 red' ]
    for (const color of colors) {
      const [amount, colorName] = color.split(' ');
      if (!(colorName in LOOKUP) ||  Number(amount) > LOOKUP[colorName as keyof typeof LOOKUP]) {
        valid = false;
        break;
      } 
    }
    if (!valid) {
      break;
    }
  }
  if (valid) {
    rtn += Number(game);
  }
}
console.log(rtn);
