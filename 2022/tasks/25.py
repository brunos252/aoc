digits = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2
}


def to_base_10(num):
    return sum(digits[num[i]] * (5**(len(num) - i - 1)) for i in range(len(num)))


def back_to_base(num_10):
    i = 1
    while 2 * (5 ** i) < num_10:
        i += 1

    num = ""
    for exp in range(i, -1, -1):
        pot = 5 ** exp
        if num_10 > 0:
            if abs(num_10 - 2 * pot) < abs(num_10 - pot):
                num += "2"
                num_10 -= 2 * pot
            elif abs(num_10 - pot) < num_10:
                num += "1"
                num_10 -= pot
            else:
                num += "0"
        else:
            if abs(num_10 + 2 * pot) < abs(num_10 + pot):
                num += "="
                num_10 += 2 * pot
            elif abs(num_10 + pot) < abs(num_10):
                num += "-"
                num_10 += pot
            else:
                num += "0"

    return num


with open("../input/25.txt") as f:
    nums = [line.strip() for line in f.readlines()]

total = 0
for num in nums:
    total += to_base_10(num)

print(total)
print(back_to_base(total))
