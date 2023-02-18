import re

class Directory:
    name: str
    files: list[tuple[str, int]]
    directories: object
    parent: object
    def __init__(self, name: str, directories):
        self.name = name
        self.files = []
        self.directories = directories
        self.parent = object()

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        else:
            return self.name == other.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Directory(name={repr(self.name)}, files count={len(self.files)}, \
directories count={repr(len(self.directories))}, parent={repr(self.parent.name if isinstance(self.parent, Directory) else '')})"

    def add_file(self, file: tuple[str, int]):
        self.files.append(file)

    def add_child(self, directory: object):
        self.directories.add(directory)
        directory.parent = self

    def size(self):
        size = 0
        for f in self.files:
            size += f[1]
        return size

    def total_size(self):
        size = self.size()
        for d in self.directories:
            size += d.total_size()
        return size

class DirectoriesCollection:
    directories: [Directory]

    def __init__(self):
        self.directories = []
    def add(self, directory: Directory):
        self.directories.append(directory)
    def contains(self, name: str):
        return self.directories.count(name) > 0
    def __getitem__(self, item):
        if isinstance(item, int):
            index = item
        else:
            index = self.directories.index(item)
        return self.directories[index]

    def __setitem__(self, key, value):
        index = self.directories.index(key)
        self.directories[index] = value

    def __len__(self):
        return len(self.directories)

    def __repr__(self):
        return f"DirectoriesCollection(count={repr(self.__len__())}, directories= \
{repr(str(self.directories))})"

    def __eq__(self, other):
        return self.directories == other.directories

def read_file(file: str):
    directories = DirectoriesCollection()
    directory: Directory
    with open('input\\' + file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('$ cd'):
                name = re.sub('\$ cd (.+)', r'\1', line)
                if name == '..':
                    directory = directory.parent
                else:
                    if 'directory' in locals() and not directory is None:
                        parent = directory
                    directory = Directory(name, DirectoriesCollection())
                    directories.add(directory)
                    if 'parent' in locals() and not parent is None:
                        parent.add_child(directory)
            elif line == '$ ls':
              pass
            elif line.startswith('dir'):
                pass
            else:
                m = re.match('^(\d+) (.+)', line)
                file_name = m.group(2)
                file_size = int(m.group(1))
                directory.add_file((file_name, file_size))
    return directories

def day7_1(file: str):
    directories = read_file(file)
    below_100k = [d.total_size() for d in directories if d.total_size() <= 100000]
    return sum(below_100k)

def day7_2(file: str):
    total_space = 70000000
    update_size = 30000000
    directories = read_file(file)
    free_space = total_space - directories[0].total_size()
    big_enough = [d.total_size() for d in directories if d.total_size() >= update_size - free_space]
    return min(big_enough)

if __name__ == "__main__":
    print(day7_2("day7.txt"))