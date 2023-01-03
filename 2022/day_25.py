lst = [list(line) for line in open('input.txt').read().split('\n')]

LOOKUP = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
in_decimal = 0
for line in lst:
    line_sum = 0
    for power, symbol in enumerate(line[::-1]):
        mult = 5 ** power
        line_sum += mult * LOOKUP[symbol]
    in_decimal += line_sum
print('in decimal:', in_decimal)

TUPLES = [('0', 0), ('1', 0), ('2', 0), ('=', 1), ('-', 1), ('0', 1)]
in_snafu = []
rem = 0
while in_decimal:
    symbol, rem = TUPLES[in_decimal%5 + rem]
    in_snafu.append(symbol)
    in_decimal = in_decimal // 5
in_snafu = ''.join(in_snafu[::-1])
print('in SNAFU:', in_snafu)
