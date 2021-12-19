from itertools import permutations
import re
from collections import Counter

scanner_regex = re.compile(r"--- scanner (\d+) ---")
beacon_regex = re.compile(r"(-?\d+),(-?\d+),(-?\d+)")


beacon_rotations = [
    lambda b: Beacon((b.x, b.z, -b.y)),
    lambda b: Beacon((-b.z, b.x, -b.y)),
    lambda b: Beacon((-b.x, -b.z, -b.y)),
    lambda b: Beacon((b.z, -b.x, -b.y)),
    lambda b: Beacon((b.z, -b.y, b.x)),
    lambda b: Beacon((b.y, b.z, b.x)),
    lambda b: Beacon((-b.z, b.y, b.x)),
    lambda b: Beacon((-b.y, -b.z, b.x)),
    lambda b: Beacon((-b.y, b.x, b.z)),
    lambda b: Beacon((-b.x, -b.y, b.z)),
    lambda b: Beacon((b.y, -b.x, b.z)),
    lambda b: Beacon((b.x, b.y, b.z)),
    lambda b: Beacon((-b.z, -b.x, b.y)),
    lambda b: Beacon((b.x, -b.z, b.y)),
    lambda b: Beacon((b.z, b.x, b.y)),
    lambda b: Beacon((-b.x, b.z, b.y)),
    lambda b: Beacon((-b.x, b.y, -b.z)),
    lambda b: Beacon((-b.y, -b.x, -b.z)),
    lambda b: Beacon((b.x, -b.y, -b.z)),
    lambda b: Beacon((b.y, b.x, -b.z)),
    lambda b: Beacon((b.y, -b.z, -b.x)),
    lambda b: Beacon((b.z, b.y, -b.x)),
    lambda b: Beacon((-b.y, b.z, -b.x)),
    lambda b: Beacon((-b.z, -b.y, -b.x))
]


class Beacon:
    def __init__(self, xyz):
        self.x, self.y, self.z = xyz
        self.conns = []

    def __repr__(self):
        return repr((self.x, self.y, self.z))

    def __sub__(self, other):
        return Beacon((self.x - other.x, self.y - other.y, self.z - other.z))

    def __add__(self, other):
        return Beacon((self.x + other.x, self.y + other.y, self.z + other.z))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))


scanners = {}

with open("19.txt") as f:
    lines = map(str.strip, f.readlines())

    try:
        while True:
            scanner_id = int(scanner_regex.match(next(lines)).group(1))
            scanners[scanner_id] = current_beacons = []
            for line in lines:
                if not line:
                    break
                current_beacons.append(Beacon(int(i) for i in beacon_regex.match(line).groups()))
    except StopIteration:
        pass


for beacon_list in scanners.values():
    for beacon, conn in permutations(beacon_list, 2):
        beacon.conns.append(conn)

known = set(scanners.pop(0))

while scanners:
    print(len(scanners))
    for scanner, beacons in scanners.items():
        for rotate in beacon_rotations:
            offsets = Counter()
            for beacon in beacons:
                offsets.update(beacon_2 - rotate(beacon) for beacon_2 in known)
            pos, in_common = offsets.most_common(1)[0]
            if in_common >= 12:
                break
        else:
            continue
        break
    else:
        continue
    del scanners[scanner]
    known.update(rotate(beacon) + pos for beacon in beacons)
print(len(known))
