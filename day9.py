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
        horizontal_distance = abs(self.x - other.x)
        vertical_distance = abs(self.y - other.y)
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

    def move_right(self):
        self.head.move(1, 0)
        horizontal_distance, vertical_distance = self.head.get_distance(self.tail)
        if horizontal_distance == 2:
            self.tail.move(1, 0)
            if vertical_distance > 0:
                self.tail.align_vertically(self.head)

    def move_left(self):
        self.head.x -= 1
        horizontal_distance, vertical_distance = self.head.get_distance(self.tail)
        if horizontal_distance == 2:
            self.tail.x -= 1
            if vertical_distance > 0:
                self.tail.y = self.head.y

    def move_up(self):
        self.head.y += 1
        horizontal_distance, vertical_distance = self.head.get_distance(self.tail)
        if vertical_distance == 2:
            self.tail.y += 1
            if horizontal_distance > 0:
                self.tail.x = self.head.x

    def move_down(self):
        self.head.y -= 1
        horizontal_distance, vertical_distance = self.head.get_distance(self.tail)
        if vertical_distance == 2:
            self.tail.y -= 1
            if horizontal_distance > 0:
                self.tail.x = self.head.x


def day9_1(file: str):
    rope = Rope()
    with open('input\\' + file, 'r') as f:
        for line in f:
            line = line.strip()
            direction, steps = line[0], int(line[2:])
            for i in range(1, steps + 1):
                match direction:
                    case "R":
                        rope.move_right()
                    case "L":
                        rope.move_left()
                    case "U":
                        rope.move_up()
                    case "D":
                        rope.move_down()
                rope.tail.log_position()
    return rope.head.get_current_position(), rope.tail.get_current_position(), rope.tail.count_positions()


if __name__ == "__main__":
    print(day9_1("day9.txt"))