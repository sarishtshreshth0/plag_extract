from collections import deque


class Dinic:

    def __init__(self, N0, N1):
        self.N0 = N0
        self.N1 = N1
        self.N = N = 2+N0+N1
        self.G = [[] for i in range(N)]
        for i in range(N0):
            forward = [2+i, 1, None]
            forward[2] = backward = [0, 0, forward]
            self.G[0].append(forward)
            self.G[2+i].append(backward)
        self.backwards = bs = []
        for i in range(N1):
            forward = [1, 1, None]
            forward[2] = backward = [2+N0+i, 0, forward]
            bs.append(backward)
            self.G[2+N0+i].append(forward)
            self.G[1].append(backward)

    def add_edge(self, fr, to):
        #assert 0 <= fr < self.N0
        #assert 0 <= to < self.N1
        v0 = 2 + fr
        v1 = 2 + self.N0 + to
        forward = [v1, 1, None]
        forward[2] = backward = [v0, 0, forward]
        self.G[v0].append(forward)
        self.G[v1].append(backward)

    def bfs(self):
        G = self.G
        level = [None]*self.N
        deq = deque([0])
        level[0] = 0
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        self.level = level
        return level[1] is not None

    def dfs(self, v, t):
        if v == t:
            return 1
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w] and self.dfs(w, t):
                e[1] = 0
                rev[1] = 1
                return 1
        return 0

    def flow(self):
        flow = 0
        while self.bfs():
            *self.it, = map(iter, self.G)
            while self.dfs(0, 1):
                flow += 1
        return flow

    def matching(self):
        return [cap for _, cap, _ in self.backwards]

#####################################################################################

N = int(input())
s = []
ss = []
for i in range(N):
    s.append([int(i) for i in input().split()])

for i in range(N):
    ss.append([int(i) for i in input().split()])

pair = []
for i in range(len(s)):
    right = []
    for j in range(N):
        if s[j][0] < ss[i][0] and s[j][1] < ss[i][1]:
            right.append(j)
    pair.append(right)

# print(pair)

#####################################################################################


# 頂点の組u,vと辺の重みc（今回は1）からグラフ作って最大流で解くFOOOOOOOOOOOOOOOOO

V = len(pair) + N + 2  # (sとt追加)

dinic = Dinic(V, V)

for i in range(len(pair)):  # 始点s（番号0）から青い点(1から最大len(pair))への辺
    u, v, c = 0, i + 1, 1
    dinic.add_edge(u, v)

for i in range(N):  # 赤い点（len(pair)+1から最大len(pair)+n）から終点t（番号V-1）への辺
    u, v, c = i + len(pair) + 1, V - 1, 1
    dinic.add_edge(u, v)

for i in range(len(pair)):  # 青い点（番号1から最大len(pair)に振り直し）から　赤い点（番号1～100に振り直し）への辺
    for j in range(len(pair[i])):
        node1, node2 = i + 1, pair[i][j] + len(pair) + 1

        u, v, c = node1, node2, 1
        dinic.add_edge(u, v)

print(dinic.flow() - 2)