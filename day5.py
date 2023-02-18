import re

class Procedure:
    from_stack: int
    number: int
    to_stack: int

    def __init__(self, from_stack: int, number: int, to_stack: int):
        self.from_stack = from_stack
        self.number = number
        self.to_stack = to_stack

    def __eq__(self, other):
        return self.from_stack == other.from_stack and \
               self.number == other.number and \
               self.to_stack == other.to_stack

    def __str__(self):
        return str([self.from_stack, self.number, self.to_stack])

    def __repr__(self):
        return f"Procedure(from_stack={repr(self.from_stack)}, number={repr(self.number)}, to_stack={repr(self.to_stack)})"

def text_to_procedure(text: str):
    match = re.match('move (?P<number>\d+) from (?P<from>\d+) to (?P<to>\d+)', text)
    return Procedure(int(match.group('from')), int(match.group('number')), int(match.group('to')))

def read_file(file: str):
    with open('input\\' + file, 'r') as f:
        file = f.readlines()
    empty_row = file.index('\n')
    crates = file[0:empty_row]
    crates.reverse()
    crates, stacks = crates[1:], crates[0]
    stacks = re.findall('\d+', stacks)
    stacks = [int(s) for s in stacks]
    stacks = dict.fromkeys(stacks)
    for c in crates:
        match = re.findall('\[[A-Z]]\s|\s{4}', c)
        i = 1
        for m in match:
            if re.match('\S', m):
                if stacks[i]:
                    stacks[i].append(m.strip())
                else:
                    stacks[i] = [m.strip()]
            i += 1
    procedure = [text_to_procedure(p) for p in file[empty_row + 1:]]

    return stacks, procedure

def get_top_of_stacks(stacks):
    top = ''
    for s in stacks.values():
        top += re.sub('\[(.)]', r'\1', s[-1])

    return top

def day5_1(file: str):
    stacks, procedure = read_file(file)

    for p in procedure:
        for i in range(p.number):
            stacks[p.to_stack].append(stacks[p.from_stack][-1])
            stacks[p.from_stack] = stacks[p.from_stack][:-1]

    return get_top_of_stacks(stacks)

def day5_2(file: str):
    stacks, procedure = read_file(file)

    for p in procedure:
        stacks[p.to_stack] = stacks[p.to_stack] + stacks[p.from_stack][-p.number:]
        stacks[p.from_stack] = stacks[p.from_stack][:-p.number]

    return get_top_of_stacks(stacks)

if __name__ == "__main__":
    print(day5_2("day5.txt"))