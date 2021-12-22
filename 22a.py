import re
from typing import Optional

regex = re.compile(r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)")


class Sector:
    def __init__(self, status, x1, x2, y1, y2, z1, z2):
        self.status = status in ["on", True]
        self.x = int(x1), int(x2)
        self.y = int(y1), int(y2)
        self.z = int(z1), int(z2)

    def __repr__(self):
        return f"Sector(status={self.status} x={self.x} y={self.y} z={self.z})"

    @property
    def volume(self):
        return (self.x[1]+1 - self.x[0]) * (self.y[1]+1 - self.y[0]) * (self.z[1]+1 - self.z[0]) * (1 if self.status else -1)

    def intersects(self, sector: "Sector") -> Optional["Sector"]:
        x = self._intersects_dim(sector, "x")
        y = self._intersects_dim(sector, "y")
        z = self._intersects_dim(sector, "z")
        if x[0] <= x[1] and y[0] <= y[1] and z[0] <= z[1]:
            return Sector(not self.status, x[0], x[1], y[0], y[1], z[0], z[1])

    def _intersects_dim(self, sector: "Sector", attr: str) -> tuple[int, int]:
        d11, d12 = getattr(self, attr)
        d21, d22 = getattr(sector, attr)
        intersect = max(d11, d21), min(d12, d22)
        return intersect

    def to_set(self):
        return {
            (x, y, z)
            for x in range(max(self.x[0], -50), min(self.x[1], 50)+1)
            for y in range(max(self.y[0], -50), min(self.y[1], 50)+1)
            for z in range(max(self.z[0], -50), min(self.z[1], 50)+1)
        }


with open("22.txt") as f:
    sectors = [Sector(*regex.match(line.strip()).groups()) for line in f.readlines()]

volume = set()
for sector in sectors:
    if sector.status:
        volume |= sector.to_set()
    else:
        volume -= sector.to_set()

print(len(volume))
