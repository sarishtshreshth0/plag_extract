from collections import Counter

class union_find():
    def __init__(self,n):
        self.n=n
        ##親要素のノード番号を格納。par[x]==xのときそのノードは根
        ##親とはその上にノードなし！！　
        self.par=[-1 for i in range(n)]
        self.rank=[0]*(n)

    def find(self,x):
        if self.par[x]<0:
            return x
        else:
            self.par[x]=self.find(self.par[x])
            
            return self.par[x]

    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)

        ##木の高さを比較し、低い方から高い方へ辺をはる
        if x==y:
          return

        if self.par[x]>self.par[y]:
          x,y=y,x
          
        self.par[x]+=self.par[y]
        self.par[y]=x

    def same(self,x,y):
        return self.find(x) == self.find(y)
    
    def size(self,x):
      return -self.par[self.find(x)]
      
    def members(self,x):
      root=self.find(x)
      return [i for i in range(self.n) if self.find(i)==root]
    
    def roots(self):
      return [i for i, x in enumerate(self.par) if x<0]
    
    def all_group_member(self):
      return {r:self.members(r) for r in self.roots()}
      
n,m,k=map(int,input().split())
uf=union_find(n)
good=[0 for _ in range(n)]
for _ in range(m):
  a,b=map(int,input().split())
  uf.union(a-1,b-1)
  good[a-1]+=1
  good[b-1]+=1
  
  
ans=[0  for _ in range(n)]
    
    
bad=[0 for _ in range(n)]
for _ in range(k):
  p,q=map(int,input().split())
  if uf.same(p-1,q-1):
    
    bad[p-1]+=1
    bad[q-1]+=1


ans1=[]
for u in range(n):
  C=uf.size(u)
  
  ans1.append(str(C-1-bad[u]-good[u]))
  
print(' '.join(ans1))