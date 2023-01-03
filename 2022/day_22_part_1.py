import re

board, instructs = open('input.txt').read().split('\n\n')
board = board.split('\n')
line_length = max([len(line) for line in board])
for idx in range(0, len(board)):
    board[idx] = list(board[idx])
    while len(board[idx]) < line_length:
       board[idx].append(' ')

instructs = re.findall(r'\d+|\w', instructs)
curr_row = 0
curr_col = board[curr_row].index('.')
facing = 'R'  # R (right), L (left), U (up), or D (down)

clockwise = ['R', 'D', 'L', 'U', 'R']
counter_clockwise = clockwise[::-1]


def one_step(row, col):
    if facing == 'R':
        if col+1 < len(board[0]) and board[row][col+1] == '.':
            col = col + 1
        elif col+1 == len(board[0]) or board[row][col+1] == ' ':
            first_wall = -1 if '#' not in board[row] else board[row].index('#')
            first_open = -1 if '.' not in board[row] else board[row].index('.')
            if first_wall == -1 or first_wall >  first_open:
                col = first_open
    elif facing == 'L':
        if col-1 >= 0 and board[row][col-1] == '.':
            col = col - 1
        elif col-1 == -1 or board[row][col-1] == ' ':
            last_wall = -1 if '#' not in board[row] else len(board[row]) - board[row][::-1].index('#') - 1
            last_open = -1 if '.' not in board[row] else len(board[row]) - board[row][::-1].index('.') - 1
            if last_wall == -1 or last_open > last_wall:
                col = last_open
    elif facing == 'D':
        if row+1 < len(board) and board[row+1][col] == '.':
            row = row + 1
        elif row+1 == len(board) or board[row+1][col] == ' ':
            for find_row in range(0, len(board)):
                if board[find_row][col] == '.':
                    row = find_row
                    break
                if board[find_row][col] == '#':
                    break
    elif facing == 'U':
        if row-1 >= 0 and board[row-1][col] == '.':
            row = row - 1
        elif row-1 == -1 or board[row-1][col] == ' ':
            for find_row in range(len(board)-1, -1, -1):
                if board[find_row][col] == '.':
                    row = find_row
                    break
                if board[find_row][col] == '#':
                    break
    return row, col


for instruct in instructs:
    if instruct.isdigit():
        for _ in range(0, int(instruct)):
            curr_row, curr_col = one_step(curr_row, curr_col)
    elif instruct == 'R':  # clockwise
        facing = clockwise[clockwise.index(facing)+1]
    elif instruct == 'L':  # counter_clockwise
        facing = counter_clockwise[counter_clockwise.index(facing)+1]

print(1000*(curr_row+1) +  4*(curr_col+1) + clockwise.index(facing))
