from collections import deque

MINS = 30
START = 'AA'
lst = [row.split('; ') for row in open('input.txt').read().split('\n')]

valves_to_keep_rates_dct = {}  # includes START valve and valves with non-zero rates
all_connections_dct = {}  # valve: [connection1, connection2]
for flow_rate, connections in lst:
    valve = flow_rate[len('Valve '):len('Valve ')+2]
    rate = int(flow_rate[len('Valve XX has flow rate='):])
    if rate > 0 or valve == START:
        valves_to_keep_rates_dct[valve] = rate
    if connections.startswith('tunnels'):
        all_connections_dct[valve] = connections[len('tunnels lead to valves '):].split(', ')
    else:
        all_connections_dct[valve] = [connections[len('tunnel leads to valve '):]]


def bfs(all_connections_dct, start_valve):
    visited = set()
    q = deque([[start_valve]])
    rtn_dct = {}
    while q:
        path = q.popleft()
        connections = all_connections_dct[path[-1]]
        for connection in connections:
            if connection != start_valve and connection not in visited:
                new_path = path + [connection]
                visited.add(connection)
                q.append(new_path)
                if connection in valves_to_keep_rates_dct.keys():
                    rtn_dct[connection] = len(new_path)-1
    return rtn_dct
precomputed_dct = {}
for valve in valves_to_keep_rates_dct.keys():
    precomputed_dct[valve] = bfs(all_connections_dct, valve)


stack = [
    [['AA'], 0, 0]  # stops, curr min, running total of released pressure
]
largest = stack[0][:]
length = len(valves_to_keep_rates_dct.keys())
while stack:
    stops, mins, ans = stack.pop()
    curr_valve = stops[-1]
    if ans > largest[2]:
        largest = [stops, mins, ans]
    if len(stops) < length:  # if we've already opened all the valves then we're done
        connections = precomputed_dct[curr_valve]
        for valve, time in connections.items():
            if valve not in stops:
                if mins + time < 30:
                    # by the time we get there and open the valve, it will be:
                    new_mins = mins + time + 1
                    remaining_mins = MINS - new_mins
                    pressure_contribution = remaining_mins * valves_to_keep_rates_dct[valve]
                    stack.append([stops+[valve], new_mins, ans+pressure_contribution])

print(largest)
