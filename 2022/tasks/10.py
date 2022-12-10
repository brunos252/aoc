clock = 1
register = 1
sig_strength = 0
CRT = ""

def tick():
    global clock, register, sig_strength, CRT
    CRT += "#" if abs((clock-1) % 40 - register) <= 1 else "."
    if clock % 40 == 20:
        sig_strength += clock * register
    clock += 1

with open("./2022/input/10.txt") as f:
    instructions = [line.split(" ") for line in f.read().strip().split("\n")]

for line in instructions:
    tick()
    if line[0] == "addx":
        tick()
        register += int(line[1])

print(sig_strength)

for i in range(6):
    print(CRT[40*i : 40*(i+1)])
