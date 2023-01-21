from itertools import product

# two kinds of sections
# 1. z ends up as 26z + inp + section_digit 
# 2. z ends up as z//26, and we need z%26 + section_digit == inp so that we're in the good case

# steps when we're in a type 1 section:
# * we need an inp to use, so try one of our bruteforce digits
# * z gets updated to 26z + inp + section_digit 
# steps when we're in a type 2 section:
# * since z%26 + section_digit = inp must hold, we can directly calculate imp from 
# our z value and section_digit
# * z gets updated to z//26

# the only things we need to get from each section are the type and section_digit
lines = open('input.txt').read().split('\n')
section_lst = []
for mult in range(0, 14):
    section = lines[mult*18:(mult+1)*18]
    type = 1 if section[4] == 'div z 1' else 2
    if type == 1:
        section_digit = int(section[-3].split(' ')[2])
    elif type == 2:
        section_digit = int(section[5].split(' ')[2])
    section_lst.append((type, section_digit))


def get_digits(input_digits):
    """Return the valid digits if they exist for this combination, otherwise None.
    """
    input_gen = (digit for digit in input_digits)
    z = 0
    ans = []

    for section_idx in range(0, 14):
        type, section_digit = section_lst[section_idx]
        if type == 1:
            inp = next(input_gen)
            ans.append(inp)
            z = 26*z + inp + section_digit
        elif type == 2: 
            # since z%26 + section_digit = inp must hold, we can directly calculate imp
            inp = z%26 + section_digit
            if inp <= 0 or inp > 9:
                return None
            ans.append(inp)
            z = z//26

    return int(''.join(map(str, ans)))


for input_digits in product([num for num in range(1, 10)], repeat=7):  # (9, 9, 9, 9, 9, 9, 9) etc
    ans = get_digits(input_digits)
    if ans is not None:
        print(ans)
        break
