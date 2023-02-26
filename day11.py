from collections import deque

class Operation:
    OPERATIONS = {
        '+': lambda a, b: a + b,
        '*': lambda a, b: a * b,
    }
    def __init__(self, operation):
        self.__text = operation
        self.__num1, operation, self.__num2 = operation.split()
        self.__operation = Operation.OPERATIONS[operation]

    @staticmethod
    def _add(a, b):
        return a + b
    @staticmethod
    def _mul(a, b):
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

class Monkey:
    monkeys = []
    worry_level_divisor = 0
    __common_divisor = 1
    @staticmethod
    def __getitem__(item):
        return Monkey.monkeys[item]

    def __init__(self, properties):
        properties[1] = properties[1][16:].replace(' ', '')
        self.items = deque([int(item) for item in properties[1].split(',')])
        self.operation = Operation(properties[2][17:])
        self.action_test = int(properties[3][19:])
        self.action_true = int(properties[4][25:])
        self.action_false = int(properties[5][26:])
        self.inspections = 0
        Monkey.monkeys.append(self)
        Monkey.__common_divisor *= self.action_test
        
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

    def play(self):
        while self.items:
            other = self.test()
            other = Monkey.monkeys[other]
            other.items += [self.items.popleft()]

    def test(self):
        self.inspections += 1
        self.items[0] %= Monkey.__common_divisor
        self.items[0] = self.operation.calc(self.items[0])
        if Monkey.worry_level_divisor > 0:
            self.items[0] //= Monkey.worry_level_divisor
        if self.items[0] % self.action_test == 0:
            return self.action_true
        else:
            return self.action_false


def read_file(file: str):
    with open('input\\' + file, 'r') as f:
        properties = [line.strip() for line in f.readlines() if line.strip() != '']
    [Monkey(properties[i:i + 6]) for i in range(0, len(properties), 6)]

def day11(file: str, rounds: int, worry_level_divisor: int):
    read_file(file)
    Monkey.worry_level_divisor = worry_level_divisor
    for i in range(rounds):
        for monkey in Monkey.monkeys:
            monkey.play()
    Monkey.monkeys.sort(reverse=True)
    return Monkey.monkeys[0].inspections * Monkey.monkeys[1].inspections

if __name__ == '__main__':
    print(day11('day11.txt', 10000, 0))