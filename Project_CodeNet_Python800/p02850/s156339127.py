import sys
sys.setrecursionlimit(10**9)

n = int(input())
neighbors = [[] for i in range(n+1)]
ab = []
for i in range(n-1):
    line = list(map(int, input().split()))
    neighbors[line[0]].append(line[1])
    neighbors[line[1]].append(line[0])
    ab.append((line[0], line[1]))
maximum = 0
neighbors_max = 0
for i in range(n):
    if maximum < len(neighbors[i]):
        neighbors_max = i
        maximum = len(neighbors[i])
edgecolors = {}
reached = {neighbors_max}
def make_other_colors(c, m):
    res = []
    if c > m:
        res += [i+1 for i in range(m)]
    else:
        res += [i+1 for i in range(c-1)]
        res += [maximum-i for i in range(m-c+1)]
    return res
def coloring(v, c):
    if c == 0:
        reached.add(v)
        for i in range(len(neighbors[v])):
            edgecolors[(v, neighbors[v][i])] = i + 1
            edgecolors[(neighbors[v][i], v)] = i + 1
            reached.add(neighbors[v][i])
            coloring(neighbors[v][i], i+1)
        return
    l = len(neighbors[v])
    if l == 1 and neighbors[v][0] in reached:
        reached.add(v)
        return
    other_colors = make_other_colors(c, l-1)
    i = 0
    j = 0
    while i < l:
        if neighbors[v][i] in reached:
            i += 1
            continue
        edgecolors[(v, neighbors[v][i])] = other_colors[j]
        edgecolors[(neighbors[v][i], v)] = other_colors[j]
        reached.add(neighbors[v][i])
        coloring(neighbors[v][i], other_colors[j])
        i += 1
        j += 1
coloring(neighbors_max, 0)
print(maximum)
for i in ab:
    print(edgecolors[i])
