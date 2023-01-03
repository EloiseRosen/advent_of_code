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


def one_step(row, col, facing):
    if facing == 'R':
        if col+1 < len(board[0]) and board[row][col+1] == '.':
            col = col + 1
        elif col+1 == len(board[0]) or board[row][col+1] == ' ':
            if row <= 49: # Right sq, going R
                new_row = 149-row
                new_col = 99
                if board[new_row][new_col] == '.':
                    row = new_row
                    col = new_col
                    facing = 'L'
            elif row >= 99 and row <= 149: # Front square, going R
                new_row = -(row-149)
                new_col = 149
                if board[new_row][new_col] == '.':
                    row = new_row
                    col = new_col
                    facing = 'L'
            elif row >= 50 and row <= 99: # Top square, going R
                new_col = row + 50
                new_row = 49
                if board[new_row][new_col] == '.':
                    row = new_row
                    col = new_col
                    facing = 'U'
            elif row >= 150: # Bottom square, going R
                new_col = row - 100
                new_row = 149
                if board[new_row][new_col] == '.':
                    row = new_row
                    col = new_col
                    facing = 'U'

    elif facing == 'L':
        if col-1 >= 0 and board[row][col-1] == '.':
            col = col - 1
        elif col-1 == -1 or board[row][col-1] == ' ':
            if row <= 49: # Back sq, going L
                new_row = 149-row   #row 0 becomes 149, row of 49 becomes row 100
                new_col = 0
                if board[new_row][new_col] == '.':
                    row = new_row
                    col = new_col
                    facing = 'R'
            elif row >= 99 and row <= 149: # Left square, going L
                new_row = -(row-149)
                new_col = 50
                if board[new_row][new_col] == '.':
                    row = new_row
                    col = new_col
                    facing = 'R'
            elif row >= 50 and row <= 99: # Top square, going L
                new_col = row - 50
                new_row = 100
                if board[new_row][new_col] == '.':
                    row = new_row
                    col = new_col
                    facing = 'D'
            elif row >= 150: # Bottom square, going L
                new_col = row - 100
                new_row = 0
                if board[new_row][new_col] == '.':
                    row = new_row
                    col = new_col
                    facing = 'D'

    elif facing == 'D':
        if row+1 < len(board) and board[row+1][col] == '.':
            row = row + 1
        elif row+1 == len(board) or board[row+1][col] == ' ':
            if col <= 49: # Bottom sq, going D
                new_row = 0
                new_col = col + 100
                if board[new_row][new_col] == '.':
                    row = new_row
                    col = new_col
                    # facing doesn't change
            elif col >= 50 and col <= 99: # Front square, going D
                new_row = col + 100  # col 50 becomes row 150 
                new_col = 49
                if board[new_row][new_col] == '.':
                    row = new_row
                    col = new_col
                    facing = 'L'
            elif col >= 99: # Right square, going D
                new_row = col - 50  
                new_col = 99
                if board[new_row][new_col] == '.':
                    row = new_row
                    col = new_col
                    facing = 'L'

    elif facing == 'U':
        if row-1 >= 0 and board[row-1][col] == '.':
            row = row - 1
        elif row-1 == -1 or board[row-1][col] == ' ':
            if col <= 49: # Left sq, going U
                new_row = col + 50 
                new_col = 50
                if board[new_row][new_col] == '.':
                    row = new_row
                    col = new_col
                    facing = 'R'
            elif col >= 50 and col <= 99: # Back square, going U
                new_row = col + 100
                new_col = 0
                if board[new_row][new_col] == '.':
                    row = new_row
                    col = new_col
                    facing = 'R'
            elif col >= 99: # Right square, going U
                new_col = col - 100
                new_row = 199
                if board[new_row][new_col] == '.':
                    row = new_row
                    col = new_col
                    # facing doesn't change

    return row, col, facing


for instruct in instructs:
    if instruct.isdigit():
        for _ in range(0, int(instruct)):
            curr_row, curr_col, facing = one_step(curr_row, curr_col, facing)
    elif instruct == 'R':  # clockwise
        facing = clockwise[clockwise.index(facing)+1]
    elif instruct == 'L':  # counter_clockwise
        facing = counter_clockwise[counter_clockwise.index(facing)+1]

print(1000*(curr_row+1) +  4*(curr_col+1) + clockwise.index(facing))
