import re
import math

START_ROBOT_INVENTORY = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
START_MATERIAL_INVENTORY = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}
lst = [line.split(':') for line in open('input.txt').read().split('\n')]
MINS = 32


# optimizations:
# 1. instead of going minute by minute, go by the 5 things we could do next:
#     A. build nothing
#     B. build an ore robot
#     C. build a clay robot
#     D. build an obsidian robot
#     E. build an geode robot  
# So if we're going down the path where we're building an obsidian robot next, get the amount of time
# we'd have to wait to gather enough resources for that, and then skip directly ahead to that point 
# where we have the obsidian robot and are at the corresponding amount of minutes
# 2. We can build only 1 robot at a time, so the max we can ever spend of a resource at once is the max
# cost in that resource. We should never have more robots of that type than that, otherwise we'll be 
# accumulating resources at a rate that is faster than is possible to spend.
def dfs(robot_inventory, material_inventory, cost_dct, robot_cap, time):
    if time == MINS+1:
        return material_inventory['geode']
    
    # there are 5 possible courses of action:
    # 1. build nothing
    # 2. build an ore robot
    # 3. build a clay robot
    # 4. build an obsidian robot
    # 5. build an geode robot   
    # if we build nothing (#1), then number of geodes is the current number we have, plus
    # the number of geode robots * the number of minutes we have left
    most_geodes = material_inventory['geode'] + robot_inventory['geode'] * (MINS-time+1)
    # also go through options #2-#5
    for robot_type, cost_dct_for_curr_robot_type in cost_dct.items():
        waiting_gives_us_more = True
        # check against robot_cap so we're not accumulating resources faster than we could spend
        if robot_type == 'geode' or robot_inventory[robot_type] < robot_cap[robot_type]:
            add_mins = 0
            for material_type, material_amount in cost_dct_for_curr_robot_type.items():
                if robot_inventory[material_type] == 0:
                    waiting_gives_us_more = False
                    break
                amount_still_needed = material_amount - material_inventory[material_type]  # total amount needed - amount we already have
                if amount_still_needed > 0:
                    add_mins = max(add_mins, math.ceil(amount_still_needed / robot_inventory[material_type]))
            if waiting_gives_us_more:
                if MINS - (time + add_mins) > 0:
                    new_robot_inventory = robot_inventory.copy()
                    new_material_inventory = material_inventory.copy()

                    # all the mining that we'd do in that time given the number of robots of each type that we have
                    for mine_robot_type, mine_robot_amount in robot_inventory.items():
                        new_material_inventory[mine_robot_type] += mine_robot_amount * (add_mins + 1) 

                    # the materials we'd use to make that robot
                    for pay_material_type, pay_material_amount in cost_dct_for_curr_robot_type.items():
                        new_material_inventory[pay_material_type] -= pay_material_amount

                    # get the new robot
                    new_robot_inventory[robot_type] += 1

                    most_geodes = max(most_geodes, dfs(new_robot_inventory, new_material_inventory, cost_dct, robot_cap, time+add_mins+1))
    return most_geodes


geodes_per_blueprint = []
for first, second in lst:
    id_num = int(re.findall(r'\d', first)[0])

    second = second.split('. ')
    
    cost_dct = {}
    cost, material = re.findall(r'\d+ \w+\b', second[0])[0].split(' ')
    cost_dct['ore'] = {material: int(cost)}

    cost, material = re.findall(r'\d+ \w+\b', second[1])[0].split(' ')
    cost_dct['clay'] = {material: int(cost)}

    cost_lst = re.findall(r'\d+ \w+\b', second[2])
    cost_dct['obsidian'] = {}
    for item in cost_lst:
        cost, material = item.split(' ')
        cost_dct['obsidian'][material] = int(cost)

    cost_lst = re.findall(r'\d+ \w+\b', second[3])
    cost_dct['geode'] = {}
    for item in cost_lst:
        cost, material = item.split(' ')
        cost_dct['geode'][material] = int(cost)

    robot_cap =  {'ore': None, 'clay': None, 'obsidian': None}
    for sub_dct in cost_dct.values():
        for material, cost in sub_dct.items():
            if robot_cap[material] is None or cost > robot_cap[material]:
                robot_cap[material] = cost

    geodes = dfs(robot_inventory=START_ROBOT_INVENTORY.copy(), material_inventory=START_MATERIAL_INVENTORY.copy(), cost_dct=cost_dct, robot_cap=robot_cap, time=1)
    geodes_per_blueprint.append(geodes)
    if id_num == 3:
        break

print(geodes_per_blueprint)
ans = 1
for geodes in geodes_per_blueprint:
    ans *= geodes
print(ans)
