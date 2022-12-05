import copy

def parse_input(lines):
    parts = lines.split("\n\n")
    crate_lines = parts[0].split("\n")
    stack_number = int(parts[0].strip()[-1])
    stacks = [[] for i in range(stack_number)]

    for i in range(len(crate_lines) - 2, -1, -1):
        for st in range(stack_number):
            crate = crate_lines[i][1 + 4 * st]
            if crate != " ":
                stacks[st].append(crate)

    orders = []
    for line in parts[1].strip().split("\n"):
        segs = line.split(" ")
        orders.append([int(segs[1]), int(segs[3])-1, int(segs[5])-1])

    return stacks, orders

with open("../input/5.txt") as f:
    stacks, orders = parse_input(f.read())

stacks2 = copy.deepcopy(stacks)

for order in orders:
    for i in range(order[0]):
        stacks[order[2]].append(stacks[order[1]].pop())

    stacks2[order[2]].extend(stacks2[order[1]][-order[0]:])
    del stacks2[order[1]][-order[0]:]

print("".join([st[-1] for st in stacks]))
print("".join([st[-1] for st in stacks2]))
