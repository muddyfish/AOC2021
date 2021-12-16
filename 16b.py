from io import StringIO
from math import prod


with open("16.txt") as f:
    hex_num = f.readline().strip()
    number = int(hex_num, 16)

bits = StringIO(bin(number)[2:].zfill(len(hex_num) * 4))


def parse_literal(bits):
    def _parse(bits):
        is_end = bits.read(1) == "0"
        number = int(bits.read(4), 2)
        if is_end:
            return 1, number
        cur, next = _parse(bits)
        return cur+1, number * 16 ** cur + next
    return _parse(bits)[1]


def decode_bits(bits):
    version = int(bits.read(3), 2)
    type_id = int(bits.read(3), 2)

    if type_id == 4:
        return parse_literal(bits)
    length_id = int(bits.read(1))
    if length_id == 0:
        total_length = int(bits.read(15), 2)
        desired_pos = bits.tell() + total_length
        subpackets = []
        while bits.tell() != desired_pos:
            subpackets.append(decode_bits(bits))
    else:
        subpacket_count = int(bits.read(11), 2)
        subpackets = [decode_bits(bits) for _ in range(subpacket_count)]
    ops = {
        0: sum,
        1: prod,
        2: min,
        3: max,
        5: lambda x: x[0] > x[1],
        6: lambda x: x[0] < x[1],
        7: lambda x: x[0] == x[1],
    }
    return ops[type_id](subpackets)


print(decode_bits(bits))