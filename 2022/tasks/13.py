from functools import cmp_to_key

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left > right:
            return -1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(len(left)):
            if i >= len(right):
                return -1
            else:
                ret = compare(left[i], right[i])
                if ret != 0:
                    return ret
        if len(right) > len(left):
            return 1
        else:
            return 0
    else:
        if isinstance(left, int):
            return compare([left], right)
        elif isinstance(right, int):
            return compare(left, [right])


with open("./2022/input/13.txt") as f:
    pairs = [list(map(eval, line.strip().split("\n"))) for line in f.read().split("\n\n")]

pairs2 = []

sum = 0
for i in range(len(pairs)):
    pairs2.extend(pairs[i])
    if compare(*pairs[i]) == 1:
        sum += (i + 1)

print(sum)

divider1 = [[2]]
divider2 = [[6]]
pairs2.append(divider1)
pairs2.append(divider2)
srt = sorted(pairs2, key=cmp_to_key(compare), reverse=True)

print((srt.index(divider1) + 1) * (srt.index(divider2) + 1))
