def parse_line(line):
    dir, amount = line.split(" ")
    amount = int(amount)
    base = {"f": (1, 0),"d": (0, 1), "u": (0, -1)}[dir[0]]
    return base[0]*amount, base[1]*amount

with open("2.txt") as f:
    dirs = [parse_line(i.strip("\n")) for i in f.readlines()]

pos = [0, 0, 0]
for x, y in dirs:
    pos[1] += y
    if x:
        pos[0] += x
        pos[2] += x * pos[1]

print(pos[0]*pos[2])