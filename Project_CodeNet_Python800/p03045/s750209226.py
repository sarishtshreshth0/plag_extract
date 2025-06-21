# E

class UnionFind():
    def __init__(self, n):
        # 根なら-size, 子なら親のIDを持つ配列
        # 最初は全て根(size:-1)として初期化する
        self.par = [-1]*n

    # 親のIDを検索する再帰関数
    def Find(self, x):
        # 親の場合、IDを返す
        if self.par[x] < 0:
            return x
        # 子の場合、その親IDで再帰呼出しする
        # 経路縮約のため、呼び出した結果で辺を張り直す
        self.par[x] = self.Find(self.par[x])
        return self.par[x]

    def Union(self, x, y):
        # 根を見つける
        x = self.Find(x)
        y = self.Find(y)

        # 同じ木だったら結合しない
        if (x==y): 
            return False
        # 常に大きい方に小さい方の木を繋げる
        if (self.par[x]>self.par[y]):
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x
        return True
    
    def isSameGroup(self, x, y):
        return self.Find(x)==self.Find(y)
    
    def Size(self, x):
        return self.par[self.Find(x)]*-1

    def Show(self):
        return self.par

n, m = map(int, input().split())

uf = UnionFind(n)

for i in range(m):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    uf.Union(x, y)

ans = 0
for i in uf.Show():
    if i<0:
        ans += 1

print(ans)