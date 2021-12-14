import re
from collections import Counter
regex = re.compile(r"(\w\w) -> (\w)")

with open("14.txt") as f:
    line = f.readline().strip()
    f.readline()

    rules = {}
    for i in f.readlines():
        match = regex.match(i.strip()).groups()
        rules[match[0]] = match[1]

rules_regex = re.compile("|".join(fr"{i}(?={j})" for i, j in rules.keys()))

for i in range(10):
    line = rules_regex.sub(lambda match: f"{line[match.span()[0]]}{rules[line[match.span()[0]:match.span()[1]+1]]}", line)

counter = Counter(line)
most_common = counter.most_common()
print(most_common[0][1] - most_common[-1][1])
