with open("../input/1.txt") as f:
    depths = list(map(int, f.readlines()))

count = 0
for i in range(1, len(depths)):
    count += int(depths[i] > depths[i-1])

print(count)

suma = sum(depths[0:3])
count2 = 0
for i in range(3, len(depths)):
    sum2 = suma - depths[i-3] + depths[i]
    count2 += int(sum2 > suma)

print (count2)

print(sum(sum(depths[i:i+3]) < sum(depths[i+1:i+4]) for i in range(0, len(depths)-3)))
