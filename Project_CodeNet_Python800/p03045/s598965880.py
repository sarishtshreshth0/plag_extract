class UnionFindBySize():
    def __init__(self, n):
        self.parents = list(range(n+1))
        self.size = [1] * (n+1)

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    # 根が同一かどうかを判定する
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.size[x] < self.size[y]:
            self.size[y] += self.size[x]
            self.parents[x] = y
        else:
            self.size[x] += self.size[y]
            self.parents[y] = x

n, m = map(int, input().split())
XY_dict = {x:[] for x in range(1, n+1)}
XYZ = []
UF = UnionFindBySize(n)

for _ in range(m):
    x, y, z = map(int, input().split())
    XY_dict[x].append(y)
    XY_dict[y].append(x)
    XYZ.append([x,y,z])

for ab in XYZ:
    a = ab[0]
    b = ab[1]
    UF.union(a,b)

Parents = UF.parents
ans = 0

for i in range(1, n+1):
    if i == Parents[i]:
        ans += 1
print(ans)