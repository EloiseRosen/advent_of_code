import sympy


points = []
for line in open('input.txt').read().split('\n'):
    pos_str, velocity_str = line.split(' @ ')
    x, y, z = list(map(int, pos_str.split(',')))
    vx, vy, vz = list(map(int, velocity_str.split(',')))
    points.append([(x, y, z), (vx, vy, vz)])

throw_x = sympy.Symbol('throw_x')
throw_y = sympy.Symbol('throw_y')
throw_z = sympy.Symbol('throw_z')
throw_vx = sympy.Symbol('throw_vx')
throw_vy = sympy.Symbol('throw_vy')
throw_vz = sympy.Symbol('throw_vz')
symbols = [throw_x, throw_y, throw_z, throw_vx, throw_vy, throw_vz]

equations = []
for idx in range(0, 3):  # we need only 3 points
    (x,y,z), (xv,vy,vz) = points[idx]
    t = sympy.Symbol('t' + str(idx))
    symbols.append(t)
    equations.append((throw_x + throw_vx*t) - (x - xv*t))
    equations.append((throw_y + throw_vy*t) - (y - vy*t))
    equations.append((throw_z + throw_vz*t) - (z - vz*t))
ans = sympy.solve(equations, *symbols)
print(sum(ans[0][0:3]))
