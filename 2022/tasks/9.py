import numpy as np

def catch_up(head, tail):
    if head[0] == tail[0]:
        if abs(head[1] - tail[1]) > 1:
            tail[1] = (head[1] + tail[1]) / 2
    elif head[1] == tail[1]:
        if abs(head[0] - tail[0]) > 1:
            tail[0] = (head[0] + tail[0]) / 2
    elif not (abs(head[0] - tail[0]) == 1 and abs(head[1] - tail[1]) == 1):
        diff = np.subtract(head, tail)
        diag = diff / np.absolute(diff)
        tail = np.add(tail, diag)

    return head, tail

def make_movement(rope, move, steps):
    visited = set()
    for _ in range(steps):
        rope[0] = np.add(rope[0], move)
        for seg in range(len(rope) - 1):
            rope[seg], rope[seg + 1] = catch_up(rope[seg], rope[seg + 1])

        visited.add((rope[-1][0], rope[-1][1]))
    
    return visited

moves = {"R": np.array([1, 0]),
        "L": np.array([-1, 0]),
        "U": np.array([0, 1]),
        "D": np.array([0, -1])}

def run(knots, motions):
    rope = np.array([[0, 0] for _ in range(knots)])

    visited = set()
    for line in motions:
        visited_move = make_movement(rope, moves[line[0]], int(line.split(" ")[1]))
        visited = visited.union(visited_move)

    return len(visited)

with open("./2022/input/9.txt") as f:
    motions = f.read().rstrip().split("\n")

    print(run(2, motions))
    print(run(10, motions))
