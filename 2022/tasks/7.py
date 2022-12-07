class Dir:
    def __init__(self, name, parent = None) -> None:
        self.name = name
        self.children = {}
        self.direct_file_len = 0
        self.parent = parent

    def get_parent(self):
        return self.parent

    def add_child(self, name: str):
        self.children[name] = Dir(name, self)

    def get_child(self, name: str):
        return self.children[name]

    def add_file(self, name: str, size: int):
        self.direct_file_len += size

    def get_size(self):
        size = self.direct_file_len
        sizes = []
        for child in self.children.values():
            sizes.extend(child.get_size())
            size += sizes[-1]

        sizes.append(size)

        return sizes

with open("../input/example.txt") as f:
    commands = [line.strip() for line in f.read().split("$")]

start_node = Dir("/")
current = start_node
for block in commands[2:]:
    lines = block.split("\n")
    if lines[0][:3] == "ls":
        for line in lines[1:]:
            if line[:3] == "dir":
                current.add_child(line[4:])
            else:
                splt = line.split(" ")
                current.add_file(splt[1], int(splt[0]))
    elif lines[0][:2] == "cd":
        if lines[0][3:] == "..":
            current = current.get_parent()
        else:
            current = current.get_child(lines[0][3:])

sizes = sorted(start_node.get_size())
free_space = 70000000 - sizes[-1]
to_delete = 30000000 - free_space

for space in sizes:
    if space > to_delete:
        print(space)
        break
