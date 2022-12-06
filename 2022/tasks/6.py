def get_unique_char_substring(line, length):
    for i in range(length, len(line)):
        if len(set(line[i-length:i])) == length:
            return i

with open("../input/6.txt") as f:
    line = f.readline().strip()

print(get_unique_char_substring(line, 4))
print(get_unique_char_substring(line, 14))
