lst = open('input.txt').read().split('\n')

# Same indices are same move. If your move is 1 index ahead of their move, you win.
their_moves = ['A', 'B', 'C']
your_move_points = [1, 2, 3, 1]  # extra entry for wrapping

win_points = 6
draw_points = 3


def get_move_points(their_move, outcome):
    their_idx = their_moves.index(their_move)
    if outcome == 'X':  # need to lose
        your_idx = their_idx-1 if their_idx-1 >= 0 else their_idx-1+3
        return your_move_points[your_idx]
    elif outcome == 'Y':  # need to draw
        return your_move_points[their_moves.index(their_move)]
    elif outcome == 'Z':  # need to win
        return your_move_points[their_idx+1]


score = 0
for line in lst:
    their_move, outcome = line.split(' ')
    score += get_move_points(their_move, outcome)
    if outcome == 'Y':
        score += draw_points
    elif outcome == 'Z':
        score += win_points
print(score)
