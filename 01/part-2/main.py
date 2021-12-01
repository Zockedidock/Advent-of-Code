#!/usr/bin/env python3

temp: int = 0
step: int = 0
count: int = 0

prev_line: int = 0

first = 0
second = 0
third = 0

with open('input') as f:
    lines = f.readlines()
    for line in lines:
        line = int(line.strip())
        step += 1
        third = second
        second = first
        first = line

        if step >= 3:
            print(first + second + third)
            print("-------")

            comb = first + second + third

            if not prev_line == 0:
                if comb > prev_line:
                    count += 1
            prev_line = int(comb)

print(count)