class Knot:
    x: int
    y: int
    positions: list

    def __init__(self):
        self.x = self.y = 1
        self.positions = list()
        self.log_position()

    def log_position(self):
        position = (self.x, self.y)
        if not self.positions.__contains__(position):
            self.positions.append(position)

    def count_positions(self):
        return len(self.positions)

    def get_current_position(self):
        return self.x, self.y

    def get_distance(self, other):
        horizontal_distance = self.x - other.x
        vertical_distance = self.y - other.y
        return horizontal_distance, vertical_distance

    def move(self, x, y):
        self.x += x
        self.y += y
        self.log_position()

    def align_horizontally(self, other):
        self.x = other.x
        self.log_position()

    def align_vertically(self, other):
        self.y = other.y
        self.log_position()


class Rope:
    head: Knot
    tail: Knot

    def __init__(self):
        self.head = Knot()
        self.tail = Knot()

    def move_horizontally(self, x):
        self.head.move(x, 0)
        horizontal_distance, vertical_distance = self.head.get_distance(self.tail)
        if abs(horizontal_distance) == 2:
            self.tail.move(x, vertical_distance)

    def move_vertically(self, y):
        self.head.move(0, y)
        horizontal_distance, vertical_distance = self.head.get_distance(self.tail)
        if abs(vertical_distance) == 2:
            self.tail.move(horizontal_distance, y)

def day9_1(file: str):
    rope = Rope()
    with open('input\\' + file, 'r') as f:
        for line in f:
            line = line.strip()
            direction, steps = line[0], int(line[2:])
            for i in range(1, steps + 1):
                match direction:
                    case "R":
                        rope.move_horizontally(1)
                    case "L":
                        rope.move_horizontally(-1)
                    case "U":
                        rope.move_vertically(1)
                    case "D":
                        rope.move_vertically(-1)
                rope.tail.log_position()
    return rope.head.get_current_position(), rope.tail.get_current_position(), rope.tail.count_positions()


if __name__ == "__main__":
    print(day9_1("day9.txt"))