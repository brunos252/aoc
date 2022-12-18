import sys

sys.setrecursionlimit(8000)


def check_within_limits(coords):
    return -1 <= coords[0] <= 20 and \
           -1 <= coords[1] <= 20 and \
           -1 <= coords[2] <= 20


def dfs(curr, cube_there, visited):
    if not check_within_limits(curr):
        return 0

    visited.add(curr)

    neighbours = [(curr[0] + 1, curr[1], curr[2]), (curr[0] - 1, curr[1], curr[2]),
                  (curr[0], curr[1] + 1, curr[2]), (curr[0], curr[1] - 1, curr[2]),
                  (curr[0], curr[1], curr[2] + 1), (curr[0], curr[1], curr[2] - 1)]

    total = 0

    for neighbour in neighbours:
        if neighbour in visited:
            continue
        if neighbour in cube_there:
            total += 1
        else:
            total += dfs(neighbour, cube_there, visited)

    return total


with open("./2022/input/18.txt") as f:
    cubes = [list(map(int, line.strip().split(","))) for line in f.readlines()]

cubes_proc = []
connections = 0

for cube in cubes:
    for proc in cubes_proc:
        if abs(cube[0] - proc[0]) + abs(cube[1] - proc[1]) + abs(cube[2] - proc[2]) == 1:
            connections += 1
    cubes_proc.append(cube)

print(6 * len(cubes) - 2 * connections)

cube_there = set(tuple(cube) for cube in cubes)

total = 0
visited = set()

start = (-1, -1, -1)
total += dfs(start, cube_there, visited)

print(total)
