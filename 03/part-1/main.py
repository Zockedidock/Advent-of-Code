
#one_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#zero_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

one_count = []
zero_count = []

gamma:str = ""
epsilon:str = ""

with open('input') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        for i in range(len(line)):
            if line[i] == '1':
                try:
                    one_count[i] += 1
                except IndexError:
                    one_count.append(1)
            else:
                try:
                    zero_count[i] += 1
                except IndexError:
                    zero_count.append(1)
    for i in range(len(one_count)):
        if one_count[i] > zero_count[i]:
            gamma += "1"
        else:
            gamma += "0"
    for bit in gamma:
        if bit == '1':
            epsilon += "0"
        else:
            epsilon += "1"
    print(f'Zero count: {zero_count}\nOne count: {one_count}\n Gamma Bits: {gamma}\n Gamma: {int(gamma, 2)}\nEpsilon Bits: {epsilon}\n Epsilon: {int(epsilon, 2)}')
    print(f'Result: {int(gamma, 2) * int(epsilon, 2)}')