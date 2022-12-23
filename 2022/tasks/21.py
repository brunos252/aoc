def parse_lines(lines: list[str]):
    tree = {}
    for line in lines:
        parts = line.strip().split(": ")
        if parts[0] == "root":
            left, _, right = parts[1].split(" ")
        tree[parts[0]] = int(parts[1]) if parts[1].isdigit() else parts[1]

    return tree, left, right


def dfs(curr: str, tree: dict):
    if not isinstance(tree[curr], int):
        elems = tree[curr].split(" ")
        tree[curr] =  int(eval(f"{dfs(elems[0], tree)} {elems[1]} {dfs(elems[2], tree)}"))

    return tree[curr]


with open("./2022/input/21.txt") as f:
    tree, left, right = parse_lines(f.readlines())

print(dfs("root", tree.copy()))

start = 0
end = 10_000_000_000_000
while True:
    i = (start + end) // 2
    tree_c = tree.copy()
    tree_c["humn"] = i
    dfs_left = dfs(left, tree_c)
    dfs_right = dfs(right, tree_c)

    if dfs_left > dfs_right:
        start = i
    elif dfs_left < dfs_right:
        end = i
    elif dfs_left == dfs_right:
        print(i)
        break
