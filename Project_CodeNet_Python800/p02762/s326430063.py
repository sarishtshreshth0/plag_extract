N,M,K=map(int,input().split())
A=[];B=[]
for i in range(M):
    a,b=map(int,input().split())
    A.append(a);B.append(b)
C=[];D=[]
for i in range(K):
    c,d=map(int,input().split())
    C.append(c);D.append(d)
f=[set() for i in range(N)]
b=[set() for i in range(N)]
for i in range(M):
    f[A[i]-1].add(B[i]-1)
    f[B[i]-1].add(A[i]-1)
for i in range(K):
    b[C[i]-1].add(D[i]-1)
    b[D[i]-1].add(C[i]-1)
checked=[False for i in range(N)]
class UnionFind:
    def __init__(self,n):
        self.n=n
        self.parents=[-1]*n
    def root(self,x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x]=self.root(self.parents[x])
            return self.parents[x]
    def union(self,x,y):
        x=self.root(x)
        y=self.root(y)
        if x==y:
            return
        if self.parents[x]>self.parents[y]:
            x,y=y,x
        self.parents[x]+=self.parents[y]
        self.parents[y]=x
    def same(self,x,y):
        return self.root(x)==self.root(y)
    def size(self,x):
        return -self.parents[self.root(x)]
    def roots(self):
        return [i for i,x in enumerate(self.parents) if x<0]
    def group_count(self):
        return len(self.roots())
uf=UnionFind(N)
for i in range(N):
    for people in f[i]:
        uf.union(i,people)
ans=[]
for i in range(N):
    c=uf.size(i)
    bl=0
    for x in b[i]:
        if uf.same(i,x):
            bl+=1
    ans.append(c-bl-1-len(f[i]))
print(*ans)