lst = open('input.txt').read().split('\n\n')

called_nums = [int(num) for num in lst[0].split(',')]

boards = []
for board in lst[1:]:
    board = board.split('\n')
    for row_idx in range(0, len(board)):
        board[row_idx] = [int(el) for el in board[row_idx].strip().split(' ') if el != '']
    boards.append(board)


def has_won(mark_board):
    for row in mark_board:
        if sum(row) == len(mark_board):
            return True
    transpose = list(map(list, zip(*mark_board)))
    for row in transpose:
        if sum(row) == len(transpose):
            return True
    return False


def calculate_score(last_num_called, board, mark_board):
    sum_of_unmarked = 0
    for row_idx in range(0, len(board)):
        for col_idx in range(0, len(board[0])):
            if mark_board[row_idx][col_idx] == 0:
                sum_of_unmarked += int(board[row_idx][col_idx])
    return sum_of_unmarked * last_num_called


def get_last_winner(called_nums, boards):
    mark_boards = [[[0]*len(boards[0][0]) for _ in range(0, len(boards[0]))] for mark_board in range(0, len(boards))]
    indicies_that_have_won = set()
    last_win_score = None
    
    for called_num in called_nums:
        for board_idx in range(0, len(boards)):
            if board_idx not in indicies_that_have_won:
                board = boards[board_idx]
                mark_board = mark_boards[board_idx]
                for row_idx in range(0, len(board)):
                    row = board[row_idx]
                    if called_num in row:
                        col_idx = row.index(called_num)
                        mark_board[row_idx][col_idx] = 1
                        if has_won(mark_board):
                            last_win_score = calculate_score(last_num_called=called_num, board=board, mark_board=mark_board)
                            indicies_that_have_won.add(board_idx)
    return last_win_score

last_win_score = get_last_winner(called_nums, boards)
print(last_win_score)
