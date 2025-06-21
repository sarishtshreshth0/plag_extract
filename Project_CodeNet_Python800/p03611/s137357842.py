n=int(input())
*a, = map(int,input().split())

#遅延セグ木で解く
class segtree:
    x_unit=0 # 要素として入れられる最大値
    def __init__(self,N):
        self.n=(1<<len(bin(N-1)[2:]))
        self.x=[self.x_unit]*(2*self.n)

    def build(self, seq):
        for i,j in enumerate(seq, start=self.n):  # n番目からseqをx配列に移していく
            self.x[i] = j
        for i in range(self.n-1, 0, -1):
            self.x[i] = 0
            # セグ木トーナメント表の左右を比較
            # 例えばn=8の時、seq[4]はx[12]に、seq[5]はx[13]に入っている
            # さらにx[14]とx[15]の間に来るのはx[7]、x[12]とx[13]の間に来るのはx[6]

    def fold(self,l,r): # 区間[l, r)値に+1 
        l+=self.n
        r+=self.n-1
        while l<r:
            if l%2==1: # lが奇数
                self.x[l]+=1
                l+=1 # 偶数に調節
            if r%2==0: # rが偶数
                self.x[r]+=1
                r-=1 # 開区間なので1個前は奇数番目の要素
            l //= 2
            r //= 2
        if l==r:
            self.x[l]+=1
        #print(self.x)
    def get(self,i): # seq[i]に対する値を取得 
        i+=self.n
        ret=self.x[i]
        while i>1:
            i //= 2
            ret+=self.x[i]
        return ret

seq=[0]*(10**5+2)
q=[(max(0, a[i]-1), min(10**5,a[i]+1)) for i in range(n)]
seg=segtree(10**5+2)
seg.build(seq)
for i in range(n):
    l,r=q[i]
    seg.fold(l,r+1)
ans=[]
for i in range(10**5+2):
    ans.append(seg.get(i))
print(max(ans))