with open("7.txt") as f:
    positions = [int(i) for i in f.read().strip().split(",")]

pos_range = range(min(positions), max(positions))
fuel_use = [sum((abs(i-pos)+abs(i-pos)**2)>>1 for i in positions) for pos in pos_range]
print(min(fuel_use))
