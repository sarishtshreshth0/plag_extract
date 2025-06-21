class unionfind():

    def __init__(self,n):
        #親番号<0なら根
        #根の場合、数値の絶対値が要素数
        self.par=[-1 for i in range(n)]
        
    def root(self,x):
        
        par=self.par
        if par[x]<0:
            return x
        else:
            self.x = self.root(par[x])
            return self.x
        
    def unite(self,x,y):
        #高いほうに低いほうをくっつける
        rx=self.root(x)
        ry=self.root(y)
        
        if rx==ry:
            return
        else:
            if self.par[rx]>self.par[ry]:
                rx,ry = ry,rx
                
            self.par[rx]+=self.par[ry]
            self.par[ry] = rx

            
    def same(self, x,y):
        return self.root(x) == self.root(y)
    
    def par_print(self):
        print(self.par)
        
    def count(self, x):
        return -self.par[self.root(x)]

n,m,k = map(int,input().split())

friend = [[] for i in range(n)]
block = [[] for i in range(n)]

uf = unionfind(n)

for i in range(m):
    
    a,b = map(int,input().split())
    a-=1
    b-=1
    
    friend[a].append(b)
    friend[b].append(a)
    
    uf.unite(a,b)
    
    
    
for i in range(k):
    
    a,b = map(int,input().split())
    a-=1
    b-=1
    
    block[a].append(b)
    block[b].append(a) 
    
    
for i in range(n):
    
    ans = uf.count(i)-1 -len(friend[i])
    
    for j in block[i]:
        if uf.same(i,j):
            ans -= 1
    
    print(ans, end = " ")
