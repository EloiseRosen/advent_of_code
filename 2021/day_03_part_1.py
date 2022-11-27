lst = open('input.txt').read().split('\n')

balance = [0 for digit in range(0, len(lst[0]))]  # 1s increment, 0s decrement
for el in lst:
    for idx in range(0, len(balance)):
        if el[idx] == '1':
            balance[idx] += 1
        else:
            balance[idx] -= 1

gamma = ''.join('1' if int(digit) > 0 else '0' for digit in balance)
epsilon = ''.join('0' if digit =='1' else '1' for digit in gamma)
print(int(gamma, 2) * int(epsilon, 2))
