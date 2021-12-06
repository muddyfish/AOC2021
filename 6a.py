from collections import Counter


def dec(fish_ages):
    return Counter({k-1: v for k, v in fish_ages.items()})


with open("6.txt") as f:
    fish_ages = Counter([int(i) for i in f.read().strip().split(",")])

for i in range(80):
    fish_ages = dec(fish_ages)
    if -1 in fish_ages:
        count = fish_ages.pop(-1)
        fish_ages[6] += count
        fish_ages[8] += count

print(sum(fish_ages.values()))
