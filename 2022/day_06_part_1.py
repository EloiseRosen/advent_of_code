string = open('input.txt').read()
for idx in range(3, len(string)):
    if len(set(string[idx-4:idx])) == 4:
        print(idx)
        break
