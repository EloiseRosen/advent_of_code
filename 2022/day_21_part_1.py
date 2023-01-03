lst = [line.split(': ') for line in open('input.txt').read().split('\n')]
dct = {}
for monkey, value in lst:
    if ' ' in value:
        dct[monkey] = value.split(' ')
    else:
        dct[monkey] = int(value)

while type(dct['root']) == list:
    for k, v in dct.items():
        if type(v) == list:
            new_v = []
            if type(dct[v[0]]) != list and type(dct[v[2]]) != list:
                if v[1] == '+':
                    dct[k] = int(dct[v[0]]) + int(dct[v[2]])
                elif v[1] == '*':
                    dct[k] = int(dct[v[0]]) * int(dct[v[2]])
                elif v[1] == '/':
                    dct[k] = int(dct[v[0]]) / int(dct[v[2]])
                elif v[1] == '-':
                    dct[k] = int(dct[v[0]]) - int(dct[v[2]])

print(dct['root'])
