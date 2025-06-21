class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    def find_root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]
        
    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if(x == y):
            return 
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
                
    def is_same_group(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def count(self, x):
        return -self.root[self.find_root(x)]
    
f=lambda:map(int,input().split())
N,M,K=f()
uf=UnionFind(N)
bro=[0]*(N+1)
AB=[]
for _ in [0]*M:
    a,b=f()
    AB.append((a,b))
    uf.unite(a,b)
for a,b in AB:
    if uf.is_same_group(a,b):
        bro[a]+=1
        bro[b]+=1
for _ in [0]*K:
    c,d=f()
    if uf.is_same_group(c,d):
        bro[c]+=1
        bro[d]+=1
for i in range(1,N+1):
    print(uf.count(i)-1-bro[i])