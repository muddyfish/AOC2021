with open("8.txt") as f:
    displays = [line.strip("\n").split(" | ")[1].split(" ") for line in f.readlines()]

print(sum(sum(1 for digit in display if len(digit) in {2, 3, 4, 7}) for display in displays))
