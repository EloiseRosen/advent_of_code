target_area_x, target_area_y = open('input.txt').read()[len('target area: '):].split(', ')
target_area_x = tuple(map(int, target_area_x[len('x='):].split('..')))
target_area_y = tuple(map(int, target_area_y[len('y='):].split('..')))

START = (0, 0)


def is_past_target(curr_x, curr_y, x_velocity, y_velocity):
    return ((y_velocity < 0 and curr_y < target_area_y[0]) or 
    (x_velocity > 0 and curr_x > target_area_x[1]))


def shoot(x_velocity, y_velocity):
    """Return boolean indicating if target area was entered, and int of max y position."""
    curr_x, curr_y = START
    max_y_reached = curr_y
    while not is_past_target(curr_x, curr_y, x_velocity, y_velocity):
        # 1. The probe's x position increases by its x velocity.
        curr_x += x_velocity

        # 2. The probe's y position increases by its y velocity.
        curr_y += y_velocity
        max_y_reached = max(max_y_reached, curr_y)

        # 3. The probe's x velocity changes by 1 toward the value 0.
        if x_velocity > 0:
            x_velocity -= 1
        if x_velocity < 0:
            x_velocity += 1

        # 4. The probe's y velocity decreases by 1.
        y_velocity -= 1

        # check if target area entered
        if (curr_x >= target_area_x[0] and curr_x <= target_area_x[1] and
        curr_y >= target_area_y[0] and curr_y <= target_area_y[1]):
            return True, max_y_reached

    return False, max_y_reached


successful_initial_velocities = set()
for try_x in range(0, target_area_x[1]+1):
    for try_y in range(target_area_y[0], abs(target_area_y[0])+1):
        entered_target, _ = shoot(try_x, try_y)
        if entered_target:
            successful_initial_velocities.add((try_x, try_y))

print(len(successful_initial_velocities))
