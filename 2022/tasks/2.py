def parse_line(line):
    line = line.rstrip().split(" ")
    return [ord(line[0])-65, ord(line[1])-88]

with open("../input/2.txt") as f:
    lines = [parse_line(line) for line in f.readlines()]

score1 = sum(line[1] + 1 + (((line[1] - line[0]) % 3 + 1) % 3) * 3 for line in lines)
score2 = sum(line[1] * 3 + (line[0] + line[1] - 1) % 3 + 1 for line in lines)

print(score1, score2)

'''
also cool to use:
    a, b = line.split()
    a = int(a.translate(str.maketrans("ABC", "123")))
    b = int(b.translate(str.maketrans("XYZ", "123")))
'''
