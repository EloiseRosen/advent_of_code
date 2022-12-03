lst = open('input.txt').read().split('\n')

# Same indices are same move. If your move is 1 index ahead of their move, you win.
their_moves = ['A', 'B', 'C']
your_moves = ['X', 'Y', 'Z', 'X']  # extra entry for wrapping
your_move_points = [1, 2, 3]

win_points = 6
draw_points = 3


def get_move(their_move, outcome):
    their_idx = their_moves.index(their_move)
    if outcome == 'X':  # need to lose
        your_idx = their_idx-1 if their_idx-1 >= 0 else their_idx-1+3
        return your_moves[your_idx]
    elif outcome == 'Y':  # need to draw
        return your_moves[their_moves.index(their_move)]
    elif outcome == 'Z':  # need to win
        return your_moves[their_idx+1]


score = 0
for line in lst:
    their_move, outcome = line.split(' ')
    your_move = get_move(their_move, outcome)
    score += your_move_points[your_moves.index(your_move)]
    if outcome == 'Y':
        score += draw_points
    elif outcome == 'Z':
        score += win_points
print(score)
