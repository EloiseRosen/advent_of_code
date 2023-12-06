import fs from 'fs';


// process input section into mapRanges array
function getMapRanges(section: string): [number, number, number][]{
  const sectionLines = section.split(':')[1].trim().split('\n'); // disregard unneeded label, split into lines
  const mapRanges: [number, number, number][] = []; // start num, end num inclusive, difference to apply
  for (const sectionLine of sectionLines) {
    const [dest, source, maxChange] = sectionLine.split(' ').map((el) => Number(el));
    const diff = dest - source;
    mapRanges.push([source, source + maxChange-1, diff]);
  }
   // our populating of the new plant values depends on mapRanges being in ascending order
  mapRanges.sort((arr1,arr2) => arr1[0]-arr2[0]);
  return mapRanges;
}


function cleanUpPriorEntry(plantRange: [number, number], 
                           mapRange: [number, number, number], 
                           newPlantRanges: [number, number][], 
                           diffs: number[]): void {
  if (newPlantRanges.length === 0) {
    newPlantRanges.push([plantRange[0], mapRange[0]-1]);
    diffs.push(0); // the prior range necessarily didn't have a mapRange match
  } else {
    const lastNewPlantRangeEnd = newPlantRanges[newPlantRanges.length-1][1];
    if (mapRange[0]-1 >= lastNewPlantRangeEnd+1) {
      newPlantRanges.push([lastNewPlantRangeEnd+1, mapRange[0]-1]);
      diffs.push(0); // the prior range necessarily didn't have a mapRange match
    }
  }
}


let input: string[] = fs.readFileSync('input.txt', 'utf8').split('\n\n');

// populate with initial seeds values
const seeds = input[0].split(': ')[1].split(' ').map((el) => Number(el));
// plantRanges is [[start of range 1, end of range 1 inclusive], [start of range 2, end of range 2 inclusive] ... ]
let plantRanges: [number, number][] = [];
for (let i = 0; i < seeds.length; i += 2) {
  plantRanges.push([seeds[i], seeds[i]+seeds[i+1]-1]);
}
input = input.slice(1); // remove initial seeds section from input array


for (const section of input) {
  const mapRanges = getMapRanges(section);

  let allNewPlantRanges: [number, number][] = [];
  for (const plantRange of plantRanges) {
    const diffs: number[] = [];
    const newPlantRanges: [number, number][] = [];

    // break plantRange into the needed pieces
    for (const mapRange of mapRanges) {
      const diff = mapRange[2];

      // mapRange completely off the left side of plantRange, so we can just go on to next mapRange
      if (mapRange[1] < plantRange[0]) {
        continue;

      // mapRange completely off the right side of plantRange, so we're done
      } else if (mapRange[0] > plantRange[1]) {
        break;

      // plantRange completely within mapRange, so after pushing plantRange we're done
      } else if (plantRange[0] >= mapRange[0] && plantRange[1] <= mapRange[1]) {
        newPlantRanges.push([plantRange[0], plantRange[1]]);
        diffs.push(diff);
        break;

      // mapRange contained completely within plantRange
      } else if (mapRange[0] >= plantRange[0] && mapRange[1] <= plantRange[1]) {
        if (plantRange[0] > 0) {
          cleanUpPriorEntry(plantRange, mapRange, newPlantRanges, diffs);
        }
        newPlantRanges.push([mapRange[0], mapRange[1]]);
        diffs.push(diff);

      // map has left overlap
      } else if (mapRange[1] <= plantRange[1]) {
        newPlantRanges.push([plantRange[0], mapRange[1]]);
        diffs.push(diff);

      // map has right overlap, so we're at end!
      } else if (mapRange[0] >= plantRange[0]) {
        cleanUpPriorEntry(plantRange, mapRange, newPlantRanges, diffs);
        newPlantRanges.push([mapRange[0], plantRange[1]]);
        diffs.push(diff);
        break;
      }
    }
    // close up end of range if needed
    if (newPlantRanges.length === 0) {
      newPlantRanges.push(plantRange);
      diffs.push(0);
    } else {
      const lastNewPlantRangeEnd = newPlantRanges[newPlantRanges.length-1][1];
      if (lastNewPlantRangeEnd !== plantRange[1]) {
        newPlantRanges.push([lastNewPlantRangeEnd+1, plantRange[1]]);
        diffs.push(0);
      }
    }

    // update the plant ranges to their new values
    const newPlantRangesAfterDiff: [number, number][] = [];
    for (let i = 0; i < diffs.length; i++) {
      const currPlantRange = newPlantRanges[i];
      const currDiff = diffs[i];
      newPlantRangesAfterDiff.push([currPlantRange[0]+currDiff, currPlantRange[1]+currDiff]);
    }
    allNewPlantRanges = [...allNewPlantRanges, ...newPlantRangesAfterDiff];
  }
  plantRanges = allNewPlantRanges;
}


let min = Number.POSITIVE_INFINITY;
for (const plantRange of plantRanges) {
  min = Math.min(min, plantRange[0]);
}
console.log(min);
