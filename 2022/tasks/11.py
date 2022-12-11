import math

def parse_lines(lines: list[str]):
    items = []
    operations = []
    divisors = []
    throw_directions = []
    for monkey in lines:
        items.append([int(item.strip()) for item in monkey[1].strip().split(" ", maxsplit=2)[2].split(", ")])
        operations.append(monkey[2].strip().split(" ", 1)[1][6:])
        divisors.append(int(monkey[3].strip().split(" ")[3]))
        throw_directions.append([int(monkey[4].strip()[-1]), int(monkey[5].strip()[-1])])

    return items, operations, divisors, throw_directions


with open("./2022/input/11.txt") as f:
    monkey_lines = [block.split("\n") for block in f.read().rstrip().split("\n\n")]

items, operations, divisors, throw_directions = parse_lines(monkey_lines)
total_inspections = [0 for _ in range(len(operations))]
MOD = math.prod(divisors)

for i in range(10000):
    for j in range(len(operations)):
        total_inspections[j] += len(items[j])
        while items[j]:
            old = items[j].pop(0)
            # new = eval(operations[j]) // 3    # part 1, for i in range(20)
            new = eval(operations[j]) % MOD
            items[throw_directions[j][bool(new % divisors[j])]].append(new)

total_inspections.sort(reverse=True)
print(total_inspections[0] * total_inspections[1])
