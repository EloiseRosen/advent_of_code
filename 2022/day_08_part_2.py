from functools import reduce

trees = [[int(el) for el in list(row)] for row in open('input.txt').read().split('\n')]
changes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

max_scenic_score = 0
for row_idx in range(1, len(trees)-1):  # can skip perimeter as always 0
    for col_idx in range(1, len(trees[0])-1):
        scenic_score_lst = []
        for row_change, col_change in changes:
            score_in_this_direction = 0
            new_row_idx = row_idx + row_change
            new_col_idx = col_idx + col_change
            while new_row_idx >= 0 and new_row_idx < len(trees) and new_col_idx >= 0 and new_col_idx < len(trees[0]):
                if trees[new_row_idx][new_col_idx] < trees[row_idx][col_idx]:
                    score_in_this_direction += 1
                elif trees[new_row_idx][new_col_idx] >= trees[row_idx][col_idx]:
                    score_in_this_direction += 1
                    break
                new_row_idx += row_change
                new_col_idx += col_change
            scenic_score_lst.append(score_in_this_direction)
        #print(scenic_score_lst)
        scenic_score = reduce(lambda x, y: x * y, scenic_score_lst)
        max_scenic_score = max(max_scenic_score, scenic_score)

print(max_scenic_score)
