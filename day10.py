class CPU:

    def __init__(self):
        self.x = 1
        self.cycles = list()
        self.__screen = ['']

    def __cycle(self, i):
        for i in range(0, i):
            cycle = len(self.cycles) + 1
            self.cycles.append(cycle * self.x)
            position = len(self.__screen[-1])
            if position == 40:
                self.__screen.append('')
                position = 1
            if abs((position - self.x)) <= 1:
                pixel = '#'
            else:
                pixel = '.'
            self.__screen[-1] += pixel

    @property
    def screen(self):
        return ''.join(l + '\n' for l in self.__screen)

    def noop(self):
        self.__cycle(1)

    def addx(self, i):
        self.__cycle(2)
        self.x += i

    def get_total_signal(self):
        total = self.cycles[19]
        x = int((len(self.cycles) - 20) / 40) + 1
        for i in range(1, x):
            total += self.cycles[19 + i * 40]
        return total

def day10_1(file: str):
    cpu = CPU()
    with open('input\\' + file, 'r') as f:
        for line in f:
            line = line.strip()
            if line == 'noop':
                cpu.noop()
            else:
                cpu.addx(int(line[5:]))
    return cpu.get_total_signal()

def day10_2(file: str):
    cpu = CPU()
    with open('input\\' + file, 'r') as f:
        for line in f:
            line = line.strip()
            if line == 'noop':
                cpu.noop()
            else:
                cpu.addx(int(line[5:]))
    return cpu.screen


if __name__ == "__main__":
    print(day10_2("day10.txt"))