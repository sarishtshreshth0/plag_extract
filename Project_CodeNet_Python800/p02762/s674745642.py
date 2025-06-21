import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

class UnionFindPathCompression():
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1]*n
        self.group_size = [1]*n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        #親を探す p = parentの意味
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return
        else:
            if self.rank[px] < self.rank[py]:
                self.parents[px] = py
                self.group_size[py] += self.group_size[px]
            else:
                self.parents[py] = px
                self.group_size[px] += self.group_size[py]
                #ランクの更新
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1
                
n,m,k = map(int,input().split())
ufpc = UnionFindPathCompression(n)
friends = [[] for i in range(n)]
ans = [-1]*n
for i in range(m):
    a, b = (int(x) for x in input().split())
    a, b = a-1, b-1
    friends[a].append(b)
    friends[b].append(a)
    ufpc.union(a,b)

for i in range(k):
    c, d = (int(x) for x in input().split())
    c, d = c-1, d-1
    if ufpc.find(c) == ufpc.find(d):
        ans[c] -= 1
        ans[d] -= 1

for i in range(n):
    ans[i] += ufpc.group_size[ufpc.find(i)]
    ans[i] -= len(friends[i])

print(*ans)