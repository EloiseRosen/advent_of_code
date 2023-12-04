import fs from 'fs';


const DIRS: [number, number][] = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, 1], [-1, 1], [1, -1]];

/**
 * Checks if there's a non-digit, non-period character adjacent to the given grid cell,
 * where "adjacent" is specified by dirs.
 */
function checkForSymbol(grid: string[], r: number, c: number, dirs: [number, number][]): boolean {
  for (const [rChange, cChange] of dirs) {
    const newR = r + rChange;
    const newC = c + cChange;
    if (newR < grid.length && newR >= 0 && newC < grid[0].length && newC >= 0 && 
      /[.\d]/.test(grid[newR][newC]) === false) {
        return true;
    }
  }
  return false;
}


const grid: string[] = fs.readFileSync('input.txt', 'utf8').split('\n');
let ans = 0;
for (let r = 0; r < grid.length; r++) {
  let c = 0;
  while (c < grid[0].length) {
    if (/\d/.test(grid[r][c])) { // found a digit
      let keep = checkForSymbol(grid, r, c, DIRS);
      let c2 = c;
      while (c2 + 1 < grid[0].length && /\d/.test(grid[r][c2+1])) { // find the rest of this number
        c2 = c2 + 1;
        if (!keep) { // if we don't have a reason to keep this number yet, check for new reasons
          keep = checkForSymbol(grid, r, c2, DIRS);
        }
      }
      if (keep) {
        const fullNum = Number(grid[r].slice(c, c2+1));
        ans += fullNum;
      }
      c = c2 + 1; // we can advance until after the number we've found
    } else {
      c++;
    }
  }
}
console.log(ans);
