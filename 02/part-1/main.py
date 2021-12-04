
horizontal: int = 0
depth:int = 0

with open('input') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith('forward'):
            horizontal += int(line[-1])
        if line.startswith('down'):
            depth += int(line[-1])
        if line.startswith('up'):
            depth -= int(line[-1])
    print(horizontal * depth)