from collections import deque


ITERATIONS = 1000


def push_button():
    """Simluates a single button push, returns number of low and high pulses."""
    low_pulses, high_pulses = 0, 0
    q = deque([])
    q.append( ('', 'broadcaster', 0) )  # sender, receiver, pulse level
    while q:
        sender, receiver, pulse = q.popleft()
        if pulse == 0:
            low_pulses += 1
        else:
            high_pulses += 1

        if receiver in modules_dct:
            if modules_dct[receiver]['type'] == '%':
                if pulse == 0:
                    for destination in modules_dct[receiver]['destination_lst']:
                        q.append( (receiver, destination, 0 if modules_dct[receiver]['is_on'] else 1) )
                    modules_dct[receiver]['is_on'] = not modules_dct[receiver]['is_on']

            elif modules_dct[receiver]['type'] == '&':
                # When a pulse is received, the conjunction module first updates its memory for that input.
                modules_dct[receiver]['inputs'][sender] = pulse
                # if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high
                pulse_to_send = 1
                if all(val == 1 for val in modules_dct[receiver]['inputs'].values()):
                    pulse_to_send = 0
                for destination in modules_dct[receiver]['destination_lst']:
                    q.append( (receiver, destination, pulse_to_send) )

            elif modules_dct[receiver]['type'] == 'broadcaster':
                for destination in modules_dct[receiver]['destination_lst']:
                    q.append( (receiver, destination, pulse) )
    return low_pulses, high_pulses


# populate module characteristics
modules_dct = {}
conjunction_modules = []
for line in open('input.txt').read().split('\n'):
    label, destinations = line.split(' -> ')
    curr_module_dct = {'destination_lst': destinations.split(', ')}
    if label[0] == '%':
        curr_module_dct['type'] = '%'
        curr_module_dct['is_on'] = False
        modules_dct[label[1:]] = curr_module_dct
    elif label[0] == '&':
        curr_module_dct['type'] = '&'
        curr_module_dct['inputs'] = {}
        modules_dct[label[1:]] = curr_module_dct
        conjunction_modules.append(label[1:])
    elif label == 'broadcaster':
        curr_module_dct['type'] = 'broadcaster'
        modules_dct['broadcaster'] = curr_module_dct

#  Conjunction modules remember the type of the most recent pulse received from each of 
# their connected input modules
for label, module_dct in modules_dct.items():
    for destination in module_dct['destination_lst']:
        if destination in conjunction_modules:
            modules_dct[destination]['inputs'][label] = 0

# count up low and high pulses
total_low_pulses, total_high_pulses = 0, 0
for _ in range(0, ITERATIONS):
    low_pulses, high_pulses = push_button()
    total_low_pulses += low_pulses
    total_high_pulses += high_pulses
print(total_low_pulses*total_high_pulses)
