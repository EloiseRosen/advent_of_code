import fs from 'fs';


// in part 2:  J cards are now the weakest cards
const CARD_ORDER = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A'];


function arraysAreSame<T>(arr1: T[], arr2: T[]): boolean {
  return arr1.length === arr2.length && arr1.every((val1, idx) => val1 === arr2[idx]);
}


function getCardCount(hand: string) {
  const cnt: Record<string, number> = {};
  for (const card of hand) {
    if (Object.keys(cnt).includes(card)) {
      cnt[card] += 1;
    } else {
      cnt[card] = 1;
    }
  }
  return cnt;
}


/**
* Retrieves hand value, with values and their descriptions as follows:
* 
* 6: Five of a kind, where all five cards have the same label: AAAAA
* 5: Four of a kind, where four cards have the same label and one card has a different label: AA8AA
* 4: Full house, where 3 cards have same label, and the remaining 2 cards share a different label: 23332
* 3: Three of a kind, where 3 cards have the same label, and the remaining 2 cards are different: TTT98
* 2: Two pair, where there are 2 pairs and the remaining card is different: 23432
* 1: One pair, where there's one pair and the other 3 cards have a different labels: A23A4
* 0: High card, where all cards' labels are distinct: 23456
*/
function handValue(hand: string) {
  const cntObj = getCardCount(hand);

  // In part 2, J cards can pretend to be whatever card is best for the purpose of determining hand type. 
  // For example, QJJQ2 is now considered four of a kind.
  if (Object.keys(cntObj).includes('J')) {
    if (cntObj.length === 1) { // 'JJJJJ' edge case
      return 6;
    }
    // get max non-J card
    let maxCard = '';
    let maxCnt = 0;
    for (const [cardType, cardCnt] of Object.entries(cntObj)) {
      if (cardType !== 'J' && cardCnt > maxCnt) {
        maxCnt = cardCnt;
        maxCard = cardType;
      }
    }
    // put the J cards into the max count category
    cntObj[maxCard] = maxCnt + cntObj['J'];
    delete cntObj['J'];
  }

  const cntArr = Object.values(cntObj).sort((a, b) => a - b);
  if (arraysAreSame(cntArr, [5])) {
    return 6;
  } else if (arraysAreSame(cntArr, [1, 4])) {
    return 5;
  } else if (arraysAreSame(cntArr, [2, 3])) {
    return 4;
  } else if (arraysAreSame(cntArr, [1, 1, 3])) {
    return 3;
  } else if (arraysAreSame(cntArr, [1, 2, 2])) {
    return 2;
  } else if (arraysAreSame(cntArr, [1, 1, 1, 2])) {
    return 1;
  } else {
    return 0;
  }
}


/**
 * Hands are sorted by hand value (e.g. five of a kind beats four of a kind). If the
 * hand values are the same, the tie is broken by which hand has the higher first card
 * value, and if those are the same then by which hand has the higher second card
 * value, etc.  If the hands are identical, 0 is returned.
 */
function sortCallback(handAndBid1: [string, number], handAndBid2: [string, number]): number {
  const hand1 = handAndBid1[0];
  const hand2 = handAndBid2[0];
  const handValue1 = handValue(hand1);
  const handValue2 = handValue(hand2);
  if (handValue1 !== handValue2) {
    return handValue1 - handValue2;
  }

  for (let i = 0; i < hand1.length; i++) {
    const card1Val = CARD_ORDER.indexOf(hand1[i]);
    const card2Val = CARD_ORDER.indexOf(hand2[i]);
    if (card1Val !== card2Val) {
      return card1Val - card2Val;
    }
  }
  return 0;
}


// process input
const input: string[][] = fs.readFileSync('input.txt', 'utf8').split('\n').map((el) => el.split(' '));
const handsAndBids: [string, number][] = [];
for (const lineArr of input) {
  handsAndBids.push([lineArr[0], Number(lineArr[1])]);
}

// sort hands
handsAndBids.sort(sortCallback);

// calculate winnings
let ans = 0;
for (let i = 0; i < handsAndBids.length; i++) {
  const rank = i + 1;
  const bid = handsAndBids[i][1];
  ans += rank * bid;
}
console.log(ans);
