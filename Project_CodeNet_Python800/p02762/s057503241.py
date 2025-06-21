class UnionFind():
    #https://note.nkmk.me/python-union-find/ 
    #note.nkmk.me  2019-08-18 
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


#初期入力、集合とユニオンファインド
import sys
input = sys.stdin.readline
N,M,K = (int(x) for x in input().split())

#接続（友好関係、ブロック関係）
uf =UnionFind(N+1)
conn_fri ={i:set() for i in range(1,N+1)}
conn_blo ={i:set() for i in range(1,N+1)}
for i in range(M):
    a,b = (int(x) for x in input().split())
    uf.union(a,b)
    conn_fri[a].add(b)
    conn_fri[b].add(a)
for i in range(K):
    c,d = (int(x) for x in input().split())
    conn_blo[c].add(d)
    conn_blo[d].add(c)

#友達候補の数＝同じグループにいる、友達関係でない、ブロック関係でない
ans ={i:0 for i in range(1,N+1)}
for i in range(1,N+1):
    root =uf.find(i)
    all =uf.size(root)
    same_groop_block =0
    for j in conn_blo[i]:
        if uf.same(i,j): #同じグループにいるけどブロック関係
            same_groop_block +=1
    ans[i] =all -len(conn_fri[i]) -same_groop_block -1 #-1 自分を引く

#出力
print(*ans.values())
#print(all)


