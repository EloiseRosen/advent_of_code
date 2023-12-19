import re


class Part:
    def __init__(self, x=None, m=None, a=None, s=None):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    def __repr__(self):
        return str(vars(self))
    
    def evaluate(self, workflows_dct):
        """Return boolean indicating whether this part is accepted under this workflow"""
        ruleset = workflows_dct['in']
        while True:
            for rule in ruleset: # e.g. ['s', '<', 1351, 'px']
                if len(rule) == 1:
                    if rule[0] == 'A':
                        return True
                    elif rule[0] == 'R':
                        return False
                    else:
                        ruleset = workflows_dct[rule[0]]
                        break
                else:
                    if rule[1] == '<':
                        if getattr(self, rule[0]) < rule[2]:
                            if rule[3] == 'A':
                                return True
                            elif rule[3] == 'R':
                                return False
                            else:
                                ruleset = workflows_dct[rule[3]]
                                break
                    else:
                        if getattr(self, rule[0]) > rule[2]:
                            if rule[3] == 'A':
                                return True
                            elif rule[3] == 'R':
                                return False
                            else:
                                ruleset = workflows_dct[rule[3]]
                                break


workflows_input, parts_input = open('input.txt').read().split('\n\n')

# populate workflows
workflows_dct = {}
for line in workflows_input.split('\n'):
    bracket = line.index('{')
    label = line[:bracket]
    final_instructs = []
    instructs = line[bracket+1:-1].split(',')
    for instruct in instructs:
        if ':' in instruct:
            condition, outcome = instruct.split(':')
            condition = re.split(r'([><])', condition) # split on > or <. Parens for capture group to keep the > or <
            condition[2] = int(condition[2])
            final_instructs.append(condition + [outcome]) # e.g. ['x', '<', 1416, 'A']
        else:
            final_instructs.append([instruct])
    workflows_dct[label] = final_instructs

# populate parts
parts = []
for line in parts_input.split('\n'):
    part = Part()
    ratings = line[1:-1].split(',')
    for rating in ratings:
        attribute_name, amount = rating.split('=')
        setattr(part, attribute_name, int(amount))
    parts.append(part)
                    
ans = 0
for part in parts:
    if part.evaluate(workflows_dct):
        ans += part.x + part.m + part.a + part.s
print(ans)
