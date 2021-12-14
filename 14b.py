import re
from collections import defaultdict
regex = re.compile(r"(\w\w) -> (\w)")


with open("14.txt") as f:
    line = f.readline().strip()
    f.readline()

    rules = {}
    for i in f.readlines():
        match = regex.match(i.strip()).groups()
        rules[match[0]] = match[1]


bigrams = defaultdict(lambda: 0)
for i, j in zip(line, line[1:]):
    bigrams[i+j] += 1


for i in range(40):
    new_bigrams = defaultdict(lambda: 0)
    for k, v in bigrams.items():
        if k in rules:
            new_bigrams[k[0] + rules[k]] += v
            new_bigrams[rules[k] + k[1]] += v
    bigrams = new_bigrams

letters = defaultdict(lambda: 0)
for k, v in bigrams.items():
    letters[k[0]] += v
    letters[k[1]] += v
values = letters.values()

print((max(values) - min(values)) / 2)
