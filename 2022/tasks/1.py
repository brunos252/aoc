with open("../input/1.txt") as f:
    lines = [line.rstrip() for line in f.readlines()]

totals = []
elf = 0
for line in lines:
    if not line:
        totals.append(elf)
        elf = 0
    else:
        elf += int(line)

totals.sort()

print(totals[-1], sum(totals[-3:]))
