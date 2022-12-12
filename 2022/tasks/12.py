def parse_input(lines: list[str]):
    grid = []
    for i in range(len(lines)):
        Sind = lines[i].find("S")
        if Sind != -1:
            start = (i, Sind)
            lines[i] = lines[i][:Sind] + "a" + lines[i][Sind + 1:]

        Eind = lines[i].find("E")
        if Eind != -1:
            end = (i, Eind)
            lines[i] = lines[i][:Eind] + "z" + lines[i][Eind + 1:]
        grid.append([ord(c)-97 for c in lines[i].strip()])

    return grid, start, end

def bfs(grid, start, end):
    current_height = 0
    visited = set()

    Q = [(start, 0)]
    visited.add(start)

    while Q:
        current, depth = Q.pop(0)
        current_height = grid[current[0]][current[1]]
        if current == end:
            return depth

        neighbours = [(current[0] + 1, current[1]), (current[0], current[1] + 1), (current[0] - 1, current[1]), (current[0], current[1] - 1)]
        for n in neighbours:
            if n not in visited and n[0] >= 0 and n[0] < len(grid) and n[1] >= 0 and n[1] < len(grid[0]) \
            and not grid[n[0]][n[1]] - current_height > 1:
                visited.add(n)
                Q.append((n, depth+1))


with open("./2022/input/12.txt") as f:
    grid, start, end = parse_input(f.readlines())

steps = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            steps.append(bfs(grid, (i, j), end))

print(bfs(grid, start, end))
print(min(i for i in steps if i))
