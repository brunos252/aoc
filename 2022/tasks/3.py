with open("../input/3.txt") as f:
    lines = f.readlines()

priorities1 = 0
for line in lines:
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    for c in firstpart:
        if c in secondpart:
            if ord(c) <= 90:
                priorities1 += ord(c) - 38
            else:
                priorities1 += ord(c) - 96
            break

priorities2 = 0
for i in range(0, len(lines), 3):
    line = lines[i]
    for c in line:
        if c in lines[i+1] and c in lines[i+2]:
            if ord(c) <= 90:
                priorities2 += ord(c) - 38
            else:
                priorities2 += ord(c) - 96
            break

print(priorities1, priorities2)
