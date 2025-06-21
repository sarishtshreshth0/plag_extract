"""
案件を報酬を受け取るまでにかかる時間で降順ソートしておく。
"""
class segTree:
    def __init__(self,n,identity):
        if bin(n).count("1") == 1:
            self.leaves = 2**(n.bit_length()-1)
        else:
            self.leaves = 2**n.bit_length()
        self.identity = identity
        self.tree = [[self.identity,-1] for i in range(self.leaves*2)]
        for i in range(self.leaves,self.leaves*2):
            self.tree[i] = [self.identity,i-self.leaves]

    def merge(self,x,y):
        #ここにマージ処理を書く
        if x[0] < y[0]:
            return x[::1]
        else:
            return y[::1]

    def update(self,i,x):
        i = i+self.leaves
        self.tree[i][0] = x
        i >>= 1
        while i > 0:
            self.tree[i] = self.merge(self.tree[i*2],self.tree[i*2+1])
            i >>= 1

    def query(self,l,r):
        #[l:r)のクエリ結果を返す
        l = l + self.leaves
        r = r + self.leaves
        res = [self.identity,-1]
        while l < r:
            if l&1:
                res = self.merge(res,self.tree[l])
                l += 1
            if r&1:
                r -= 1
                res = self.merge(res,self.tree[r])
            l >>= 1
            r >>= 1
        return res

N,M = map(int,input().split())
M += 1
sgt = segTree(N,float("INF"))
AB = [list(map(int,input().split())) for _ in range(N)]
AB.sort(key=lambda x: -x[0])

today = 1
for i in range(N):
    a,b = AB[i]
    due = M-a
    #M日までに報酬を受け取るためには、何日までに働かなくてはいけないかを求める。

    if today <= due:
        #今日の日付がdue以下であれば、今日その仕事をこなす
        sgt.update(today-1,b)
        today += 1
    else:
        if due < 1:
            continue
        #今日の日付がdueを過ぎてしまっている場合は、due以前の労働で報酬がb以下の仕事のうち、報酬がもっとも低い仕事を塗り替える。
        tmp = sgt.query(0,due)
        if tmp[0] < b:
            sgt.update(tmp[1],b)
        
ans = 0
for i in range(N):
    if sgt.tree[i+sgt.leaves][0] != float("INF"):
        ans += sgt.tree[i+sgt.leaves][0]
print(ans)


