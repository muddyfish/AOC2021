import json
import math
import copy
from itertools import permutations


class Done(Exception): pass


class MutableInt:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return repr(self.value)

    def __add__(self, other):
        return MutableInt(self.value + other.value)

    def __iadd__(self, other):
        self.value += other.value
        return self

    def __gt__(self, other):
        return self.value > other


with open("18.txt") as f:
    lines = [json.loads(i.strip(), parse_int=lambda x: MutableInt(int(x))) for i in f.readlines()]


def _repr(line):
    return repr(line).replace(" ", "")


def flatten(lst):
    rtn = []
    for i in lst:
        if isinstance(i, list):
            rtn.extend(flatten(i))
        else:
            rtn.append(i)
    return rtn


def do_explode(i, line, flattened):
    pair = line[i]
    flattened_index = flattened.index(pair[0])
    if flattened_index != 0:
        flattened[flattened_index - 1] += pair[0]
    if flattened_index != len(flattened) - 2:
        flattened[flattened_index + 2] += pair[1]
    line[i] = MutableInt(0)
    flattened[flattened_index: flattened_index+2] = [line[i]]


def do_split(i, line, flattened):
    value = line[i]
    flattened_index = flattened.index(value)
    halved = value.value / 2
    line[i] = [MutableInt(int(math.floor(halved))), MutableInt(int(math.ceil(halved)))]
    flattened[flattened_index:flattened_index+1] = line[i]


def reduce_line(line: list, flattened: list[MutableInt], depth: int = 0, *, do_splits: bool):
    for i, value in enumerate(line):
        if isinstance(value, list):
            if depth == 3:
                do_explode(i, line, flattened)
                raise Done()
            else:
                line[i] = reduce_line(value, flattened, depth + 1, do_splits=do_splits)
        elif value > 9 and do_splits:
            do_split(i, line, flattened)
            raise Done()
    return line


def full_reduce(current_line: list):
    flattened = flatten(current_line)
    while True:
        try:
            current_line = reduce_line(current_line, flattened, do_splits=False)
            current_line = reduce_line(current_line, flattened, do_splits=True)
        except Done:
            pass
        else:
            return current_line


def get_magnitude(line) -> int:
    if isinstance(line, MutableInt):
        return line.value
    left, right = line
    return 3 * get_magnitude(left) + 2 * get_magnitude(right)


mag = 0
for line in permutations(lines, 2):
    mag = max(mag, get_magnitude(full_reduce(copy.deepcopy(list(line)))))
print(mag)
