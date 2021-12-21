with open("21.txt") as f:
    player_1_start = int(f.readline()[-2])
    player_2_start = int(f.readline()[-1])


def deterministic_dice():
    i = 0
    while True:
        i += 1
        yield i
        if i == 100:
            i = 0

dice = deterministic_dice()

player_pos = [player_1_start, player_2_start]
player_scores = [0, 0]
turn = 0
while max(player_scores) < 1000:
    player = turn % 2
    player_pos[player] = (player_pos[player] + next(dice) + next(dice) + next(dice)) % 10
    if player_pos[player] == 0:
        player_pos[player] = 10
    player_scores[player] += player_pos[player]

    turn += 1

print(min(player_scores) * turn * 3)
