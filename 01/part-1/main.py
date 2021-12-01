#!/usr/bin/env python3

last_line: int = 0
count: int = 0

with open('input') as f:
    lines = f.readlines()
    for line in lines:
        line = int(line.strip())
        print(line)

        if not last_line == 0:
            if line > last_line:
                count += 1            

        last_line = int(line)

print(f"\nlast: {last_line} \ncount: {count}")