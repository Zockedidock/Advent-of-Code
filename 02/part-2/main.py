
horizontal: int = 0
depth:int = 0
aim: int = 0

with open('input') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith('forward'):
            horizontal += int(line[-1])
            depth += aim * int(line[-1])
        if line.startswith('down'):
            aim += int(line[-1])
        if line.startswith('up'):
            aim -= int(line[-1])
    print(horizontal * depth)