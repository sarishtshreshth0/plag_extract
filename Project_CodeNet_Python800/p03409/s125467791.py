from collections import deque


class Dinic:
    """
    1-indexed
    din = Dinic(N)
    for _ in range(M):
        s,t,cap = map(int,input().split())
        din.add_edge(s,t,cap)
    ans = din.get_maximumFlow(source, sink)
    """

    def __init__(self, N):
        self.N = N
        self.edge = [[] for _ in range(N + 1)]
        self.level = [-1] * (N + 1)

    def add_edge(self, v_from, v_to, cap):
        self.edge[v_from].append([v_to, cap, len(self.edge[v_to])])
        self.edge[v_to].append([v_from, 0, len(self.edge[v_from]) - 1])

    def _BFS(self, s):
        """
        sからの最短距離をBFSで計算する  
        """
        level = [-1] * (self.N + 1)
        level[s] = 0
        que = deque([s])
        while que:
            s = que.popleft()
            for t, cap, _ in self.edge[s]:
                if cap > 0 and level[t] < 0:
                    level[t] = level[s] + 1
                    que.append(t)
        self.level = level[:]

    def _DFS(self, v, goal, f):
        """
        増加パスをDFSで探す
        """
        if v == goal:
            return f
        for i in range(self.iterate[v], len(self.edge[v])):
            self.iterate[v] = i
            to, cap, rev = self.edge[v][i]
            if cap > 0 and self.level[v] < self.level[to]:
                d = self._DFS(to, goal, min(cap, f))
                if d > 0:
                    self.edge[v][i][1] -= d
                    self.edge[to][rev][1] += d
                    return d
        return 0

    def get_maximumFlow(self, s, t):
        """
        s -> tの最大流を求める
        1-indexed
        """
        self.goal = t
        inf = 10**18
        flow = 0
        while True:
            self._BFS(s)
            if self.level[t] < 0:
                return flow
            self.iterate = [0] * (self.N + 1)
            while True:
                f = self._DFS(s, t, inf)
                if f <= 0:
                    break
                flow += f


if __name__ == "__main__":
    N = int(input())
    din = Dinic(2 * N + 10)
    red = [tuple(map(int, input().split())) for _ in range(N)]
    blue = [tuple(map(int, input().split())) for _ in range(N)]

    source = 2 * N + 1
    sink = source + 1

    for i, (xi, yi) in enumerate(red):
        for j, (xj, yj) in enumerate(blue):
            if xi < xj and yi < yj:
                s = i + 1
                t = j + 1 + N
                din.add_edge(s, t, 1)
    for i in range(1, N + 1):
        din.add_edge(source, i, 1)
        din.add_edge(i + N, sink, 1)

    ans = din.get_maximumFlow(source, sink)
    print(ans)
