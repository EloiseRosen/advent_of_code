lst = [line.split(': ') for line in open('input.txt').read().split('\n')]
dct = {}
for monkey, value in lst:
    if monkey != 'humn':
        if monkey == 'root':
            value = value.split(' ')
            equal_from_root = [value[0], value[2]]
        elif ' ' in value:
            dct[monkey] = value.split(' ')
        else:
            dct[monkey] = int(value)

changed = True
while changed:
    changed = False
    for k, v in dct.items():
        if type(v) == list:
            if v[0] in dct and type(dct[v[0]]) != list:
                dct[k][0] = dct[v[0]]
            if v[2] in dct and type(dct[v[2]]) != list:
                dct[k][2] = dct[v[2]]
            if type(dct[k][0]) == int and type(dct[k][2]) == int:
                changed = True
                if dct[k][1] == '+':
                    dct[k] = dct[k][0] + dct[k][2]
                elif dct[k][1] == '*':
                    dct[k] = dct[k][0] * dct[k][2]
                elif dct[k][1] == '/':
                    dct[k] = dct[k][0] // dct[k][2]
                elif dct[k][1] == '-':
                    dct[k] = dct[k][0] - dct[k][2]


def recursive_solve(key):
    expression = dct[key] if key in dct else key

    if type(expression) == int:
        return expression
    else:
        term1 = recursive_solve(expression[0])
        op = expression[1]
        term2 = recursive_solve(expression[2])
        if op == '+':
            dct[key] = term1 + term2
            return dct[key]
        elif op == '-':
            dct[key] = term1 - term2
            return dct[key]
        elif op == '*':
            dct[key] = term1 * term2
            return dct[key]
        else:
            dct[key] = term1 // term2
            return dct[key]


def algebra(term1, term2):
    num = dct[term2] if term2 in dct else term2
    if type(num) != int:  # need to swap
        term1, term2 = term2, term1
        num = term2
    expression = dct[term1] if type(term1) != list else term1
        
    if type(expression[0]) == str and type(expression[2]) == str:
        try:
            result = recursive_solve(expression[0])
            dct[expression[0]] = result
            expression[0] = result
        except RecursionError:  # on non-human side
            result = recursive_solve(expression[2])
            dct[expression[2]] = result
            expression[2] = result

    if '/' in expression:
        if type(expression[2]) == int:
            return [expression[0], num * (expression[2])]
        else:
            return [expression[2], num * (expression[0])]
    elif '+' in expression:
        if type(expression[2]) == int:
            return [expression[0], num-(expression[2])]
        else:
            return [expression[2], num-(expression[0])]
    elif '*' in expression:
        if type(expression[2]) == int:
            return [expression[0], num//(expression[2])]
        else:
            return [expression[2], num//(expression[0])]
    elif '-' in expression:
        if type(expression[2]) == int:
            return [expression[0], num+(expression[2])]
        else:
            return [expression[2], -(num-(expression[0]))]


nonhuman_side = recursive_solve(equal_from_root[1])
dct[equal_from_root[1]] = nonhuman_side

if type(dct[equal_from_root[0]]) == int:
    also_equal = algebra(equal_from_root[1], equal_from_root[0])
else:
    also_equal = algebra(equal_from_root[0], equal_from_root[1])
while also_equal[0] != 'humn':
    also_equal = algebra(dct[also_equal[0]], also_equal[1])
print(also_equal[1])
