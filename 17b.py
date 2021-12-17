import re

regex = re.compile(r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)")

with open("17.txt") as f:
    data = regex.match(f.readline().strip())
    x1, x2, y1, y2 = map(int, data.groups())


def simulate_step(position, velocity):
    position[0] += velocity[0]
    position[1] += velocity[1]

    if velocity[0] > 0:
        velocity[0] -= 1
    elif velocity[0] < 0:
        velocity[0] += 1
    velocity[1] -= 1
    return position, velocity


def run_simulation(velocity):
    position = [0, 0]
    while True:
        position, velocity = simulate_step(position, velocity)
        if x1 <= position[0] <= x2 and y1 <= position[1] <= y2:
            return True
        if position[0] > x2 or position[1] < y1:
            return False


# Y always reaches y=0 on the way down. The next step needs to be just in the target area
max_y = (-1 - y1)

successes = 0
for x in range(x2+1):
    for y in range(y1, max_y+1):
        if run_simulation([x, y]):
            successes += 1

print(successes)
