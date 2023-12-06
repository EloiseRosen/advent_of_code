import fs from 'fs';


let input: string[] = fs.readFileSync('input.txt', 'utf8').split('\n\n');

// populate initial seeds values
const allMappings = input[0].split(': ')[1].split(' ').map((el) => [Number(el)]);
input = input.slice(1);

for (const section of input) {
  const sectionLines = section.split(':')[1].trim().split('\n'); // disregard unneeded label, split into lines
  for (let mappingIdx = 0; mappingIdx < allMappings.length; mappingIdx++) {
    const currMapping = allMappings[mappingIdx];
    const currVal = currMapping[currMapping.length-1];
    for (const sectionLine of sectionLines) {
      const [dest, source, maxChange] = sectionLine.split(' ').map((el) => Number(el));
      if (currVal >= source && currVal < source + maxChange) {
        const diff = dest - source;
        const newVal = currVal + diff;
        allMappings[mappingIdx].push(newVal);
        break;
      }
    }
  }
}
let min = Number.POSITIVE_INFINITY;
for (const subArr of allMappings) {
  min = Math.min(subArr[subArr.length-1], min);
}
console.log(min);
