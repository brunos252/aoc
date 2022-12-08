import numpy as np

def find_max_changes(numbers):
    max = -1
    updated_max = [False] * len(numbers)
    for i in range(len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
            updated_max[i] = True

    return updated_max

def pass_left_right(trees):
    dim = len(trees)
    visible = np.array([[0] * dim] * dim)
    for i in range(dim):
        row = np.copy(trees[i])
        visible[i] = find_max_changes(row)
        row = np.flip(row)
        visible[i] = np.logical_or(visible[i], np.flip(find_max_changes(row)))

    return visible

with open("./2022/input/8.txt") as f:
    trees = np.array([[int(x) for x in line.rstrip()] for line in f.readlines()])

visible = pass_left_right(trees)
trees = np.rot90(trees)
visible = np.logical_or(visible, np.rot90(pass_left_right(trees), 3))
print(visible.sum())


with open("./2022/input/8.txt") as f:
    trees = [[int(x) for x in line.rstrip()] for line in f.readlines()]

dim = len(trees)

scenic_score = [[1 for _ in range(dim)] for _ in range(dim)]

for i in range(dim):
    for j in range(dim):
        count = 0
        for k in range(j+1, dim):
            count += 1
            if trees[i][k] >= trees[i][j] or k == dim-1:
                scenic_score[i][j] = scenic_score[i][j] * count
                break

        count = 0
        for k in range(j-1, -1, -1):
            count += 1
            if trees[i][k] >= trees[i][j] or k == 0:
                scenic_score[i][j] = scenic_score[i][j] * count
                break

        count = 0
        for k in range(i+1, dim):
            count += 1
            if trees[k][j] >= trees[i][j] or k == dim-1:
                scenic_score[i][j] = scenic_score[i][j] * count
                break

        count = 0
        for k in range(i-1, -1, -1):
            count += 1
            if trees[k][j] >= trees[i][j] or k == 0:
                scenic_score[i][j] = scenic_score[i][j] * count
                break

print(max(map(max, scenic_score)))
