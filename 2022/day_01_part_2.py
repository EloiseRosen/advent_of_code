lst = open('input.txt').read().split('\n\n')

totals = []
for sublst in lst:
    totals.append(sum(map(int, sublst.split('\n'))))
totals.sort(reverse=True)
print(sum(totals[:3]))
