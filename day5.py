import re

class Procedure:
    fromstack: int
    number: int
    tostack: int

    def __init__(self, fromstack: int, number: int, tostack: int):
        self.fromstack = fromstack
        self.number = number
        self.tostack = tostack

    def __eq__(self, other):
        return self.fromstack == other.fromstack and \
               self.number == other.number and \
               self.tostack == other.tostack

    def __str__(self):
        return str([self.fromstack, self.number, self.tostack])

    def __repr__(self):
        return f"Procedure(fromstack={repr(self.fromstack)}, number={repr(self.number)}, tostack={repr(self.tostack)})"

def text_to_procedure(text: str):
    match = re.match('move (?P<number>\d+) from (?P<from>\d+) to (?P<to>\d+)', text)
    return Procedure(int(match.group('from')), int(match.group('number')), int(match.group('to')))

def read_file(file: str):
    with open('input\\' + file, 'r') as f:
        file = f.readlines()
    emptyRow = file.index('\n')
    crates = file[0:emptyRow]
    crates.reverse()
    crates, stacks = crates[1:], crates[0]
    stacks = re.findall('\d+', stacks)
    stacks = [int(s) for s in stacks]
    stacks = dict.fromkeys(stacks)
    for c in crates:
        match = re.findall('\[[A-Z]]\s|\s{4}', c)
        for m in match:
            i = match.index(m) + 1
            if re.match('\S', m):
                if stacks[i]:
                    stacks[i].append(m.strip())
                else:
                    stacks[i] = [m.strip()]
    procedure = [text_to_procedure(p) for p in file[emptyRow + 1:]]

    return stacks, procedure

def day5_1(file: str):
    stacks, procedure = read_file(file)

    for p in procedure:
        for i in range(p.number):
            stacks[p.tostack].append(stacks[p.fromstack][-1])
            stacks[p.fromstack] = stacks[p.fromstack][:-1]

    return stacks

if __name__ == "__main__":
    print(day5_1("day5.txt"))