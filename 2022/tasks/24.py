from queue import PriorityQueue


def move_blizzards(blizzards: list[list], grid, dim_x, dim_y):
    blizzards.append([])
    for blizzard, direction in blizzards[-2]:
        if direction == ">":
            if grid[blizzard[0]][blizzard[1] + 1] == "#":
                blizzards[-1].append([(blizzard[0], 1), ">"])
            else:
                blizzards[-1].append([(blizzard[0], blizzard[1] + 1), ">"])
        elif direction == "<":
            if grid[blizzard[0]][blizzard[1] - 1] == "#":
                blizzards[-1].append([(blizzard[0], dim_x - 2), "<"])
            else:
                blizzards[-1].append([(blizzard[0], blizzard[1] - 1), "<"])
        elif direction == "^":
            if grid[blizzard[0] - 1][blizzard[1]] == "#":
                blizzards[-1].append([(dim_y - 2, blizzard[1]), "^"])
            else:
                blizzards[-1].append([(blizzard[0] - 1, blizzard[1]), "^"])
        elif direction == "v":
            if grid[blizzard[0] + 1][blizzard[1]] == "#":
                blizzards[-1].append([(1, blizzard[1]), "v"])
            else:
                blizzards[-1].append([(blizzard[0] + 1, blizzard[1]), "v"])


def get_priority(curr, end, depth):
    return depth + abs(curr[0] - end[0]) + abs(curr[1] - end[1])


def make_trip(start, end, blizzards, grid, dim_x, dim_y, neighbours, start_depth = 0):
    pq = PriorityQueue()
    pq.put((get_priority(end, start, start_depth), (start, start_depth)))
    visited = {(start, start_depth)}

    while pq:
        curr, depth = pq.get()[1]
        visited.add((curr, depth))
        if depth + 2 > len(blizzards):
            move_blizzards(blizzards, grid, dim_x, dim_y)
        if curr == start:
            if start[0] == 0:
                pq.put((get_priority(end, (1, 1), depth + 1), ((1, 1), depth + 1)))
            else:
                pq.put((get_priority(end, (start[0] - 1, start[1]), depth + 1), ((start[0] - 1, start[1]), depth + 1)))
            continue

        for n in neighbours:
            neigh = (curr[0] + n[0], curr[1] + n[1])
            if (neigh, depth + 1) in visited:
                continue
            if neigh == end:
                return depth + 1

            if grid[neigh[0]][neigh[1]] != "#":
                for blizz in blizzards[depth + 1]:
                    if blizz[0] == neigh:
                        break
                else:
                    pq.put((get_priority(end, neigh, depth + 1), (neigh, depth + 1)))
                    visited.add((neigh, depth + 1))


with open("../input/24.txt") as f:
    grid = [line.strip() for line in f.readlines()]

start = (0, 1)
end = (len(grid) - 1, len(grid[0]) - 2)

blizzards = [[]]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != "." and grid[i][j] != "#":
            blizzards[0].append([(i, j), grid[i][j]])

dim_y = len(grid)
dim_x = len(grid[0])

# third neighbour represents waiting
neighbours = ((1, 0), (0, 1), (0, 0), (-1, 0), (0, -1))

steps_1 = make_trip(start, end, blizzards, grid, dim_x, dim_y, neighbours)
steps_2 = make_trip(end, start, blizzards, grid, dim_x, dim_y, neighbours, steps_1)
steps_3 = make_trip(start, end, blizzards, grid, dim_x, dim_y, neighbours, steps_2)

print(steps_1)
print(steps_2)

