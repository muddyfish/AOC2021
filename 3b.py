with open("3.txt") as f:
    lines = [l.strip() for l in f.readlines()]


def mode(values):
    count_0 = values.count("0")
    count_1 = values.count("1")
    return "0" if count_0 > count_1 else "1"


oxy = lines
for i in range(len(oxy[0])):
    most_common = mode("".join(j[i] for j in oxy))
    oxy = [j for j in oxy if j[i] == most_common]
    if len(oxy) == 1:
        break
co2 = lines
for i in range(len(lines[0])):
    least_common = "10"[int(mode("".join(j[i] for j in co2)))]
    co2 = [j for j in co2 if j[i] == least_common]
    if len(co2) == 1:
        break

print(int("".join(oxy), 2) * int("".join(co2), 2))
