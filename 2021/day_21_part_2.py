from collections import defaultdict

END_CONDITION = 21
pawn_pos = tuple(int(row[len('Player X starting position: '):]) for row in open('input.txt').read().split('\n'))
scores = (0, 0)

die_sum_occurrences = defaultdict(lambda: 0)  # sum of 3 die rolls: occurrences
for i in [1, 2, 3]:
    for j in [1, 2, 3]:
        for k in [1, 2, 3]:
            die_sum_occurrences[sum([i, j, k])] += 1


memo = {}  # ((pawn_pos_1, pawn_pos_2), (score_1, score_2)): (number of wins 1, number of wins 2)
def get_win_count_per_player(original_pawn_pos, original_scores):  # idx 0 of these is current player
    if (original_pawn_pos, original_scores) in memo:
        return memo[((original_pawn_pos, original_scores))]

    if original_scores[0] >= END_CONDITION:
        return [1, 0]
    elif original_scores[1] >= END_CONDITION:
        return [0, 1]

    win_count_per_player = [0, 0]
    for three_die_total, occurrences in die_sum_occurrences.items():
        curr_player_pawn_pos, other_player_pawn_pos = original_pawn_pos
        curr_player_score, other_player_score = original_scores
        
        spaces_to_move = three_die_total
        curr_player_pawn_pos += spaces_to_move
        curr_player_pawn_pos = (curr_player_pawn_pos - 1) % 10 + 1

        curr_player_score += curr_player_pawn_pos

        wins_1, wins_2 = get_win_count_per_player((other_player_pawn_pos, curr_player_pawn_pos), 
                                                  (other_player_score, curr_player_score))
        win_count_per_player[0] += wins_2 * occurrences
        win_count_per_player[1] += wins_1 * occurrences
    memo[((original_pawn_pos, original_scores))] = win_count_per_player
    return win_count_per_player


wins_1, wins_2 = get_win_count_per_player(pawn_pos, scores)
print(wins_1, wins_2)
print(max(wins_1, wins_2))
