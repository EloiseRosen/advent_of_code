from collections import deque

points = {tuple(map(int, row.split(','))) for row in open('input.txt').read().split('\n')}
final_to_include = points.copy()
dirs = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]


def get_surface_area(points):
    ans = 0
    for x, y, z in points:
        for x_change, y_change, z_change in dirs:
            new_x = x + x_change
            new_y = y + y_change
            new_z = z + z_change
            if (new_x, new_y, new_z) not in points:
                ans += 1
    return ans


# bounds
min_x = min(points, key=lambda x: x[0])[0]
max_x = max(points, key=lambda x: x[0])[0]
min_y = min(points, key=lambda x: x[1])[1]
max_y = max(points, key=lambda x: x[1])[1]
min_z = min(points, key=lambda x: x[2])[2]
max_z = max(points, key=lambda x: x[2])[2]

for x, y, z in points:
    for x_change, y_change, z_change in dirs:
        new_x = x + x_change
        new_y = y + y_change
        new_z = z + z_change
        if (new_x, new_y, new_z) not in points:
            point = (new_x, new_y, new_z)
            out_of_bounds = False
            if point not in points:
                q = deque([point])
                visited = set()
                visited.add(point)

                while q:
                    curr_point = q.popleft()
                    curr_x, curr_y, curr_z = curr_point

                    if (curr_x < min_x or curr_x > max_x or 
                    curr_y < min_y or curr_y > max_y or
                    curr_z < min_z or curr_z > max_z):
                        out_of_bounds = True
                        break

                    for x_change, y_change, z_change in dirs:
                        new_x = curr_x + x_change
                        new_y = curr_y + y_change
                        new_z = curr_z + z_change
                        if ((new_x, new_y, new_z) not in points 
                        and (new_x, new_y, new_z) not in visited):
                            q.append((new_x, new_y, new_z))
                            visited.add((new_x, new_y, new_z))
                            
                if not out_of_bounds:
                    final_to_include.update(visited)

print(get_surface_area(final_to_include))
