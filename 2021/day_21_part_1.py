from itertools import cycle

END_CONDITION = 1000
die = cycle(i for i in range(1, 101))
player_1_turn = True
die_rolls = 0
pawn_pos = [int(row[len('Player X starting position: '):]) for row in open('input.txt').read().split('\n')]
scores = [0, 0]

while True:
    spaces_to_move = next(die) + next(die) + next(die)
    die_rolls += 3
    idx = 0 if player_1_turn else 1
    pawn_pos[idx] += spaces_to_move
    pawn_pos[idx] = (pawn_pos[idx] - 1) % 10 + 1
    scores[idx] += pawn_pos[idx]

    if scores[idx] >= END_CONDITION:
        break

    player_1_turn = not player_1_turn

losing_idx = 1 if player_1_turn else 0
print(scores[losing_idx], die_rolls, scores[losing_idx] * die_rolls)
