with open("../input/4.txt") as f:
    lines = [line.rstrip().split(",") for line in f.readlines()]

subsets = 0
overlaps = 0
for line in lines:
    pair1 = [int(n) for n in line[0].split("-")]
    pair2 = [int(n) for n in line[1].split("-")]

    if pair1[0] <= pair2[0] and pair1[1] >= pair2[1] or \
            pair1[0] >= pair2[0] and pair1[1] <= pair2[1]:
        subsets += 1

    if pair1[1] >= pair2[0] and pair1[0] <= pair2[1]:
        overlaps += 1

print(subsets, overlaps)

