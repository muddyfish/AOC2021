with open("8.txt") as f:
    displays = [line.strip("\n") for line in f.readlines()]

acc = 0
for display in displays:
    digits, displayed = display.split(" | ")
    digits = ["".join(sorted(s)) for s in digits.split(" ")]
    displayed = ["".join(sorted(s)) for s in displayed.split(" ")]

    digits_dict = {}
    reverse_dict = {}
    for d in digits:
        if len(d) == 2:
            digits_dict[d] = 1
            reverse_dict[1] = set(d)
        elif len(d) == 3:
            digits_dict[d] = 7
            reverse_dict[7] = set(d)
        elif len(d) == 4:
            digits_dict[d] = 4
            reverse_dict[4] = set(d)
        elif len(d) == 7:
            digits_dict[d] = 8
            reverse_dict[8] = set(d)
    for d in digits:
        if d in digits_dict:
            continue
        # 5 - 2, 3, 5
        # 6 - 0, 6, 9
        intersects = [len(set(d) & reverse_dict[1]), len(set(d) & reverse_dict[4])]
        if len(d) == 5:
            if intersects[0] == 2:
                digits_dict[d] = 3
            elif intersects[1] == 2:
                digits_dict[d] = 2
            elif intersects[1] == 3:
                digits_dict[d] = 5
        else:
            if intersects[0] == 1:
                digits_dict[d] = 6
            elif intersects[1] == 3:
                digits_dict[d] = 0
            elif intersects[1] == 4:
                digits_dict[d] = 9
    assert set(digits_dict.values()) == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    acc += int("".join(str(digits_dict[d]) for d in displayed))

print(acc)

