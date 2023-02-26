from collections import deque

monkeys = list()

class Operation:

    def __init__(self, operation):
        self.__text = operation
        self.__num1, operation, self.__num2 = operation.split()
        if operation == '*':
            self.__operation = self._mul
        else:
            self.__operation = self._add

    def _add(self, a, b):
        return a + b
    def _mul(self, a, b):
        return a * b
    def __eq__(self, other):
        return self.__text == str(other)
    def __str__(self):
        return self.__text

    def __repr__(self):
        return f"Operation(number 1={repr(self.__num1)}, number 2={repr(self.__num2)}, \
operation={repr(self.__text)})"

    def calc(self, old):
        a = old if self.__num1 == 'old' else int(self.__num1)
        b = old if self.__num2 == 'old' else int(self.__num2)
        return self.__operation(a, b)

class Item:

    def __init__(self, worry_level):
        self.worry_level = int(worry_level)

    def __eq__(self, other):
        return self.worry_level == other.worry_level

    def __int__(self):
        return self.worry_level

    def __add__(self, other):
        if isinstance(other, Item):
            other = other.worry_level
        return Item(self.worry_level + other)

    def __mul__(self, other):
        if isinstance(other, Item):
            other = other.worry_level
        return Item(self.worry_level * other)

    def __truediv__(self, other):
        if isinstance(other, Item):
            other = other.worry_level
        return Item(self.worry_level / other)

    def __str__(self):
        return str(self.worry_level)

    def __repr__(self):
        return f'Item(worry_level={repr(self.worry_level)})'
class Monkey:

    def __init__(self, properties):
        properties[1] = properties[1][16:].replace(' ', '')
        self.items = deque([Item(item) for item in properties[1].split(',')])
        self.operation = Operation(properties[2][17:])
        self.action_test = int(properties[3][19:])
        self.action_true = int(properties[4][25:])
        self.action_false = int(properties[5][26:])
        self.inspections = 0
        monkeys.append(self)
        
    def __eq__(self, other):
        return self.items == other.items and self.operation == other.operation and \
        self.action_test == other.test and self.action_true == other.action_true and \
        self.action_false == other.action_false

    def __gt__(self, other):
        return self.inspections > other.inspections

    def __lt__(self, other):
        return self.inspections < other.inspections
    def __str__(self):
        return str([self.items, self.operation, self.action_test, self.action_true, self.action_false])

    def __repr__(self):
        return f"Monkey(items={repr(self.items)}, operation={repr(self.operation)}, \
test={repr(self.action_test)}, action_true={repr(self.action_true)} , action_false=\
{repr(self.action_false)}, inspections={repr(self.inspections)})"

    def play(self, worry_level_divider):
        while len(self.items) > 0:
            item = self.items[0]
            other = self.test(item, worry_level_divider)
            other = monkeys[other]
            other.items.append(self.items.popleft())
    def test(self, item, worry_level_divider):
        self.inspections += 1
        item.worry_level = self.operation.calc(item.worry_level)
        if worry_level_divider > 0:
            item.worry_level = item.worry_level // worry_level_divider
        if item.worry_level % self.action_test == 0:
            return self.action_true
        else:
            return self.action_false

def read_file(file: str):
    with open('input\\' + file, 'r') as f:
        properties = f.readlines()
    properties = [line.strip() for line in properties if line.strip() != '']
    monkeys_count = int(len(properties) / 6)
    for i in range(0, monkeys_count):
        start = i * 6
        end = start + 6
        Monkey(properties[start:end])

def day11(file: str, rounds: int, worry_level_divider: int):
    read_file(file)
    for i in range(0, rounds):
        for monkey in monkeys:
            monkey.play(worry_level_divider)
    monkeys.sort(reverse=True)
    return monkeys[0].inspections * monkeys[1].inspections

if __name__ == '__main__':
    print(day11('day11t.txt', 10000, 0))