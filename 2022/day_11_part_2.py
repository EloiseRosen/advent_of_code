ROUNDS = 10_000
input_lst = [monkey.split('\n') for monkey in open('input.txt').read().split('\n\n')]


class Monkey:
    def __init__(self, item_lst, operation_lst, div_test, true_throw, false_throw):
        self.item_lst = item_lst
        self.operation_lst = operation_lst  # [term1, op, term2]
        self.div_test = div_test
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.num_inspected_items = 0

    def __repr__(self):
        string = f"""
        item_lst: {self.item_lst}
        operation_lst: {self.operation_lst}
        div_test: {self.div_test} 
        true_throw: {self.true_throw}
        false_throw: {self.false_throw}
        self.num_inspected_items: {self.num_inspected_items}
        """
        return string

    def inspect_item(self, old):
        self.num_inspected_items += 1
        first, op, second = self.operation_lst
        if first == 'old':
            first = old
        if second == 'old':
            second = old
        if op == '+':
            return int(first) + int(second)
        elif op == '*':
            return int(first) * int(second)

    def get_throw_index(self, num):
        return self.false_throw if num%self.div_test else self.true_throw

mod = 1
monkeys = []  # the monkey number corresponds to the index
for monkey in input_lst:
    item_lst = list(map(int, monkey[1].strip()[len('Starting items: '):].split(', ')))
    operation_lst = monkey[2].strip()[len('Operation: new = '):].split(' ')
    div_test = int(monkey[3].strip()[len('Test: divisible by '):])
    mod *= div_test
    true_throw = int(monkey[4].strip()[len('If true: throw to monkey '):])
    false_throw = int(monkey[5].strip()[len('If false: throw to monkey '):])
    monkeys.append(Monkey(item_lst=item_lst, 
        operation_lst=operation_lst, 
        div_test=div_test, 
        true_throw=true_throw, 
        false_throw=false_throw))

for _ in range(0, ROUNDS):
    for monkey in monkeys:
        while monkey.item_lst:
            old = monkey.item_lst.pop(0)
            new = monkey.inspect_item(old)
            new = new % mod
            throw_idx = monkey.get_throw_index(new)
            monkeys[throw_idx].item_lst.append(new)

num_inspected_items_lst = [monkey.num_inspected_items for monkey in monkeys]
num_inspected_items_lst.sort(reverse=True)
print(num_inspected_items_lst[0] * num_inspected_items_lst[1])
