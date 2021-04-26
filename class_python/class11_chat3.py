import os

lines = []
with open('read/3.txt', 'r', encoding='utf-8-sig') as f:
    lines = [line.strip() for line in f]

print(lines)
new_lines = [line.split(' ') for line in lines]
for line in new_lines:
    time = line[0][:5]
    name = line[0][5:]
    print(time, name)
