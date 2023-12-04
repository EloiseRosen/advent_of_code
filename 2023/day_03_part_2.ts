import fs from 'fs';


/**
 * Retrieve the number that starts at the given grid position (grid[r][c]). Number can be 
 * retrieved going left or right as specified by goLeft.
 */
function getLeftOrRightNum(grid: string[], r: number, c: number, goLeft: boolean): string {
  const change = goLeft ? -1 : 1;
  let c2 = c;
  while (c2+change >= 0 && c2+change < grid[0].length && /\d/.test(grid[r][c2+change])) {
    c2 = c2 + change;
  }
  return c2 > c ? grid[r].slice(c, c2+1) : grid[r].slice(c2, c+1);
}


const grid: string[] = fs.readFileSync('input.txt', 'utf8').split('\n');
let ans = 0;
for (let r = 0; r < grid.length; r++) {
  for (let c = 0; c < grid[0].length; c++) {
    if (grid[r][c] === '*') {
      const nums: number[] = [];

      // left and right
      for (const cChange of [-1, 1]) {
        if (c+cChange >= 0 && c+cChange < grid[0].length && /\d/.test(grid[r][c+cChange])) {
          nums.push(Number(getLeftOrRightNum(grid, r, c+cChange, cChange===-1)));
        }
      }

      // up and down, including one over to catch diagonals
      for (const rChange of [-1, 1]) {
        // if there's a number in the middle, check to left and right and combine without double-counting middle digit
        if (r+rChange >= 0 && r+rChange < grid.length && /\d/.test(grid[r+rChange][c])) {
          const left = getLeftOrRightNum(grid, r+rChange, c, true);
          const right = getLeftOrRightNum(grid, r+rChange, c, false);
          nums.push(Number(left + right.slice(1)));
        } else { // no number in middle, so just check left and right
          for (const cChange of [-1, 1]) {
            if (r+rChange >= 0 && r+rChange < grid.length && c+cChange >= 0 && c+cChange < grid[0].length 
              && /\d/.test(grid[r+rChange][c+cChange])) {
              nums.push(Number(getLeftOrRightNum(grid, r+rChange, c+cChange, cChange===-1)));
            }
          }
        }
      }
      if (nums.length >= 2) {
        ans += nums.reduce((acc, val) => acc * val, 1);
      }
    }
  }
}
console.log(ans);
