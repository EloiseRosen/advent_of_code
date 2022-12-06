NUM_DISTINCT = 14

string = open('input.txt').read()
for idx in range(NUM_DISTINCT-1, len(string)):
    if len(set(string[idx-NUM_DISTINCT:idx])) == NUM_DISTINCT:
        print(idx)
        break
