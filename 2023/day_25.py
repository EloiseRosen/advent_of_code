from collections import deque
import networkx as nx


connections_dct = {}
graph = nx.DiGraph()
for line in open('input.txt').read().split('\n'):
    from_, tos = line.split(': ')
    tos = tos.split(' ')
    for to in tos:
        graph.add_edge(from_, to)
        graph.add_edge(to, from_)
        if from_ not in connections_dct:
            connections_dct[from_] = set()
        if to not in connections_dct:
            connections_dct[to] = set()
        connections_dct[from_].add(to)
        connections_dct[to].add(from_)

# get which wires to cut
wires_to_cut = nx.minimum_edge_cut(graph)
print(wires_to_cut)

# cut wires
for from_, to in list(wires_to_cut):
    connections_dct[from_].discard(to)
    connections_dct[to].discard(from_)

# get size of the two parts
# if we go all possible paths from here, how many components do we see?
start = from_
seen = set()
q = deque([])
q.append(start)
while q:
    curr = q.popleft()
    seen.add(curr)
    for child in connections_dct[curr]:
        if child not in seen:
            q.append(child)
size1 = len(seen)
size2 = len(connections_dct.keys())-len(seen)
print(size1, size2, size1*size2)
