
class UnionFind():
    #要素数nで初期化
    #インスタンス変数の初期化
    def __init__(self, n):
        #root : 木の要素数
        #rnk : 木の高さ(rank)
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)
    
    """ノードxのrootノードを見つける"""
    def Find_Root(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x]) 
            return self.root[x]
    
    """木の合併"""
    def Union(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        
        #既に同じ木に所属する場合
        if (x==y):
            return 
        
        #異なる木に所属する場合
        elif (self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            
            #rnkが同じ場合
            if self.rnk[x]==self.rnk[y]:
                self.rnk[y] += 1
    
    """xとyが同じグループに所属するか"""
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)
    
    """ノードxが属する木のサイズ"""
    def Count(self, x):
        return -self.root[self.Find_Root(x)]
    
n,m = map(int,input().split())
uf = UnionFind(n)
for i in range(m):
    x,y,z = map(int,input().split())
    uf.Union(x-1, y-1)
tank = set([])
for i in range(n):
    tank.add(uf.Find_Root(i))
print(len(tank))