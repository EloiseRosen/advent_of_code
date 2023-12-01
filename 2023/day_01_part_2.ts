import fs from 'fs';

const LOOKUP = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9',
};


function checkNumberMatch(s: string, i: number): string | null {
  if (/[0-9]/.test(s[i])) {
    return s[i];
  } 
  for (const [word, digit] of Object.entries(LOOKUP)) {
    if (s.slice(i,).startsWith(word)) {
      return digit;
    }
  }
  return null;
}


const arr: string[] = fs.readFileSync('input.txt', 'utf8').split('\n');
let rtn = 0;
for (const s of arr) {
  let first = '', last = '';
  for (let i = 0; i < s.length; i++) {
    const result = checkNumberMatch(s, i);
    if (result !== null) {
      first = result;
      break;
    }
  }
  for (let i = s.length - 1; i > -1; i--) {
    const result = checkNumberMatch(s, i);
    if (result !== null) {
      last = result;
      break;
    }
  }
  rtn += Number(first + last);
}
console.log(rtn);
