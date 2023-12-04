import fs from 'fs';

const arr: string[] = fs.readFileSync('input.txt', 'utf8').split('\n');

let ans = 0;
const regex = /[0-9]/;
for (const s of arr) {
  let first = '', last = '';
  for (let i = 0; i < s.length; i++) {
    if (regex.test(s[i])) {
      first = s[i];
      break;
    }
  }
  for (let i = s.length - 1; i > -1; i--) {
    if (regex.test(s[i])) {
      last = s[i];
      break;
    }
  }
  ans += Number(first + last);
}

console.log(ans);
