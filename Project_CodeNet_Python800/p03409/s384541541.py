import sys
input = sys.stdin.readline

class Dinic:
    def __init__(self, len_X, len_Y):
        self.len_X, self.len_Y = len_X, len_Y
        self.edges = [[] for _ in range(len_X)]
        self.matched = [-1] * len_Y
        self.visited = set()

    def add_edge(self, x, y):
        self.edges[x].append(y)

    def dfs(self, x):
        """
        :param x: X側の未マッチングの頂点の1つ
        :param visited: 空のsetを渡す（外部からの呼び出し時）
        :return: 増大路が見つかればTrue
        """
        for next_x in self.edges[x]:
            if next_x in self.visited:
                continue
            self.visited.add(next_x)
            if self.matched[next_x] == -1 or self.dfs(self.matched[next_x]):
                self.matched[next_x] = x
                return True
        return False

    def solve(self):
        """ 増大路発見に成功したらTrue(=1)。合計することでマッチング数となる """
        res = 0
        for x in range(self.len_X):
            self.visited = set()
            res += self.dfs(x)
        return res

#################################################################################################

N = int(input())

X = []
Y = []
for i in range(N):
    X.append([int(i) for i in input().split()])

for i in range(N):
    Y.append([int(i) for i in input().split()])

dinic = Dinic(len(X), len(Y))

for i in range(len(X)):
    for j in range(N):
        if X[i][0] < Y[j][0] and X[i][1] < Y[j][1]:
            dinic.add_edge(i, j)

print(dinic.solve())
