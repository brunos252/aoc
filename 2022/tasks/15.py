ROW_NUMBER = 2000000
GRID_DIM = 4000000

import re

with open("./2022/input/15.txt") as f:
    coords = [list(map(int, re.findall('-?[0-9]+', line))) for line in f.readlines()]

sensors = [[elem[0], elem[1]] for elem in coords]
beacons = [[elem[2], elem[3]] for elem in coords]

dists = [(abs(elem[0] - elem[2]) + abs(elem[1] - elem[3])) for elem in coords]

grid_x = sorted([(sensors[i][0] + dists[i]) for i in range(len(sensors))])[-1]
shift_x = -sorted([(sensors[i][0] - dists[i]) for i in range(len(sensors))])[0]

row = ["." for _ in range(grid_x + shift_x)]
   
for i in range(len(sensors)):
    diff = abs(sensors[i][1] - ROW_NUMBER)
    r = dists[i] - diff
    if r >= 0:
        left_ind = max(sensors[i][0] - r + shift_x, 0)
        right_ind = min(sensors[i][0] + r + shift_x, grid_x + shift_x - 1)
        row[left_ind: right_ind + 1] = ["#"] * (right_ind - left_ind + 1)

    if beacons[i][1] == ROW_NUMBER:
        row[beacons[i][0] + shift_x] = "B"
    if sensors[i][1] == ROW_NUMBER:
        row[sensors[i][0] + shift_x] = "S"

print(row.count("#"))

for j in range(GRID_DIM):
    limits = dict()
    for i in range(len(sensors)):
        diff = abs(sensors[i][1] - j)
        r = dists[i] - diff
        if r > 0:
            left_ind = max(sensors[i][0] - r, 0)
            right_ind = min(sensors[i][0] + r, GRID_DIM)
            limits[left_ind] = limits.get(left_ind, 0) + 1
            limits[right_ind] = limits.get(right_ind, 0) - 1

    count = 0
    for k in sorted(limits.items()):
        count += k[1]
        if count <= 0 and k[0] < GRID_DIM - 1:
            print("gottem", (k[0] + 1) * GRID_DIM + j)
            exit()
