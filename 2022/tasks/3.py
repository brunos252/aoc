with open("../input/3.txt") as f:
    lines = f.readlines()

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

priorities = 0
for line in lines:
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    for c in firstpart:
        if c in secondpart:
            if ord(c) <= 90:
                priorities += upper.index(c) + 27
            else:
                priorities += lower.index(c) + 1
            break

print(priorities)

priorities = 0
for i in range(0, len(lines), 3):
    line = lines[i]
    for c in line:
        if c in lines[i+1] and c in lines[i+2]:
            if ord(c) <= 90:
                priorities += upper.index(c) + 27
            else:
                priorities += lower.index(c) + 1
            break

print(priorities)
