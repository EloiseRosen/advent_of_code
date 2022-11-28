lst = open('input.txt').read().split('\n')
count_matrix = [[0]*1000 for _ in range(0, 1000)]
for el in lst:
    start, end = el.split('->')
    start_x, start_y = map(int, start.strip().split(','))
    end_x, end_y = map(int, end.strip().split(','))
    if start_x == end_x:  # vertical
        for curr_y in range(min(start_y, end_y), max(start_y, end_y)+1):
            count_matrix[curr_y][start_x] += 1
    if start_y == end_y:  # horizontal
        for curr_x in range(min(start_x, end_x), max(start_x, end_x)+1):
            count_matrix[start_y][curr_x] += 1

ans = 0
for row in count_matrix:
    ans += sum(el > 1 for el in row) 
print(ans)
