from typing import List
import functools

with open("21.txt") as f:
    player_1_start = int(f.readline()[-2])
    player_2_start = int(f.readline()[-1])


@functools.lru_cache(maxsize=None)
def run_universe(player_pos, player_scores) -> List[int]:
    if max(player_scores) >= 21:
        return [player_scores[0] >= 21, player_scores[1] >= 21]

    winners = [0, 0]
    # [sum(i) for i in itertools.product((1, 2, 3), repeat=3)], summed by count
    for count, dice_sum in ((1, 3), (3, 4), (6, 5), (7, 6), (6, 7), (3, 8), (1, 9)):
        new_player_pos = (player_pos[1], player_pos[0] + dice_sum)
        if new_player_pos[1] > 10:
            new_player_pos = (new_player_pos[0], new_player_pos[1] - 10)
        # Already swapped the positions
        new_player_scores = (player_scores[1], player_scores[0] + new_player_pos[1])
        game_winners = run_universe(new_player_pos, new_player_scores)
        winners[0] += count * game_winners[1]
        winners[1] += count * game_winners[0]
    return winners


winners = run_universe((player_1_start, player_2_start), (0, 0))
print(max(winners))
