ITER = 1000000000000

def move_LR(shape, move):
    shape_mv = []
    for point in shape:
        shape_mv.append((point[0], point[1] + move))
        if shape_mv[-1][1] < 0 or shape_mv[-1][1] > 6:
            return shape

    return shape_mv

def move_UD(shape, move):
    return [(point[0] + move, point[1]) for point in shape]
    

with open("./2022/input/17.txt") as f:
    moves = [1 if c == ">" else -1 for c in f.read().strip()]

shapes = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(1, 0), (1, 1), (0, 1), (2, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (1, 0), (1, 1)]
]

fallen = set()
fallen.update([(-1, 0), (-1, 1), (-1, 2), (-1, 3), (-1, 4), (-1, 5), (-1, 6)])

highest = -1
last_highest = -1
last_i = -1
moves_ind = 0

rot_flag = False
skip_first_moves_rotation = True

i = 0
while i < ITER:

    # this if block is skipping iterations for part 2
    if rot_flag:
        if skip_first_moves_rotation:
            skip_first_moves_rotation = False
        else:
            delta_i = i - last_i
            delta_h = highest - last_highest
            rotations = ((ITER - i) // delta_i)
    
            highest = highest + rotations * delta_h
            i = i + rotations * delta_i
            fallen = set((j + rotations * delta_h, i) for (j, i) in fallen)

        last_highest = highest
        last_i = i
        rot_flag = False

    shape = move_UD(shapes[i % 5][:], highest + 4)
    shape = move_LR(shape, 2)
    while True:
        shape_try = move_LR(shape, moves[moves_ind])
        moves_ind += 1
        if moves_ind == len(moves):
            rot_flag = True
            moves_ind = 0

        if len(fallen.intersection(set(shape_try))) == 0:
            shape = shape_try[:]

        shape_try = move_UD(shape, -1)

        if len(fallen.intersection(set(shape_try))) > 0:
            fallen = fallen.union(shape)
            for j in range(len(shape)):
                highest = max(highest, shape[j][0])            
            break

        shape = shape_try

    i += 1
    if i == 2022:
        print("part1: ", highest + 1)

print("part2: ", highest + 1)
