lst = open('input.txt').read().split('\n')

# Same indices are same move. If your move is 1 index ahead of their move, you win.
their_moves = ['A', 'B', 'C']
your_moves = ['X', 'Y', 'Z', 'X']  # extra entry for wrapping
your_move_points = [1, 2, 3]

win_points = 6
draw_points = 3

score = 0
for line in lst:
    them, you = line.split(' ')
    them_idx = their_moves.index(them)
    you_idx = your_moves.index(you)
    score += your_move_points[you_idx]
    if them_idx == you_idx:
        score += draw_points
    elif your_moves[them_idx+1] == you:
        score += win_points      
print(score)
