lst = open('input.txt').read().split('\n')
count_matrix = [[0]*1000 for _ in range(0, 1000)]
for el in lst:
    start, end = el.split('->')
    start_x, start_y = map(int, start.strip().split(','))
    end_x, end_y = map(int, end.strip().split(','))
    if start_x == end_x:  # vertical line has undefined slope
        for curr_y in range(min(start_y, end_y), max(start_y, end_y)+1):
            count_matrix[curr_y][start_x] += 1
    else:
        slope = int((start_y-end_y) / (start_x-end_x))
        if start_x > end_x:  # start should have the smallest x value
            start_x, end_x = end_x, start_x
            start_y, end_y =  end_y, start_y
    
        curr_x, curr_y = start_x, start_y
        while curr_x <= end_x:
            count_matrix[curr_y][curr_x] += 1
            curr_x += 1
            curr_y += slope

ans = 0
for row in count_matrix:
    ans += sum(el > 1 for el in row) 
print(ans)
