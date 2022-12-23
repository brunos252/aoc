moves = [[[-1, -1], [-1, 0], [-1, 1]], 
        [[1, -1], [1, 0], [1, 1]], 
        [[1, -1], [0, -1], [-1, -1]], 
        [[-1, 1], [0, 1], [1, 1]]]

def get_propositions(elves) -> dict:
    global moves
    propositions = {}
    for elf in elves:
        adj = False
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0:
                    continue
                if [elf[0] + i, elf[1] + j] in elves:
                    adj = True
                    break
            if adj:
                break 

        if not adj:
            continue 

        for move in moves:
            if [elf[0] + move[0][0], elf[1] + move[0][1]] not in elves and \
                [elf[0] + move[1][0], elf[1] + move[1][1]] not in elves and \
                [elf[0] + move[2][0], elf[1] + move[2][1]] not in elves:
                middle = (elf[0] + move[1][0], elf[1] + move[1][1])
                if middle in propositions:
                    propositions.pop(middle)
                else:
                    propositions[middle] = elf
                break

    moves = moves[1:] + moves[:1]

    return propositions


def get_limits(elves):
    limits = [[elves[0][0], elves[0][0]], [elves[0][1], elves[0][1]]]
    for elf in elves:
        if elf[0] < limits[0][0]:
            limits[0][0] = elf[0]
        elif elf[0] > limits[0][1]:
            limits[0][1] = elf[0]

        if elf[1] < limits[1][0]:
            limits[1][0] = elf[1]
        elif elf[1] > limits[1][1]:
            limits[1][1] = elf[1]
        
    return limits

def get_empty(limits, elves):
    return (limits[0][1] - limits[0][0] + 1) * (limits[1][1] - limits[1][0] + 1) - len(elves)

with open("./2022/input/23.txt") as f:
    grid = [line.strip() for line in f.readlines()]

elves = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "#":
            elves.append([i, j])

#part2 > 12 min
i = 1
while True:
    elves_past = elves[:]
    proposed: dict = get_propositions(elves)
    elves.extend([list(prop) for prop in proposed.keys()])
    for value in proposed.values():
        elves.remove(value)
    
    if elves_past == elves:
        print(i)
        break

    if i == 10:
        limits = get_limits(elves)
        print(get_empty(limits, elves))

    i = i + 1
