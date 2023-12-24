from itertools import combinations


START = 200000000000000
END = 400000000000000
points = []
for line in open('input.txt').read().split('\n'):
    pos_str, velocity_str = line.split(' @ ')
    x, y, _ = list(map(int, pos_str.split(',')))
    vx, vy, _ = list(map(int, velocity_str.split(',')))
    points.append([(x, y), (vx, vy)])

ans = 0
for point1, point2 in combinations(points, 2):
    (x1, y1), (vx1, vy1) = point1
    (x2, y2), (vx2, vy2) = point2

    try:
        p1 = (vy2*(x1-x2) - vx2*(y1-y2)) // (vy1*vx2 - vx1*vy2)
        p2 = (vy1*(x2-x1) - vx1*(y2-y1)) // (vy2*vx1 - vx2*vy1)
        intersection_x = x1 + p1*vx1
        intersection_y = y1 + p1*vy1
    except ZeroDivisionError:
        continue

    # does the intersection point occur in the forward direction of both points' movement paths, and
    # fall within the needed area?
    if (p1 >= 0 and p2 >= 0 and 
        intersection_x >= START and intersection_x <= END and 
        intersection_y >= START and intersection_y <= END):
        ans += 1
print(ans)
