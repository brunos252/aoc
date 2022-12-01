with open("../input/2.txt") as f:
    ins = [line.split(" ") for line in f.readlines()]

posX = 0
posY = 0
aim = 0
for lst in ins:
    if lst[0] == "forward":
        posX += int(lst[1])
        posY += aim * int(lst[1])
    elif lst[0] == "down":
        aim += int(lst[1])
    else:
        aim -= int(lst[1])

print(posX * aim)
print(posX * posY)
