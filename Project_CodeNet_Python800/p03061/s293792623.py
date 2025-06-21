import math
INF=float('inf')

n=int(input())
A=list(map(int,input().split()))

class SegmentTree:
    def __init__(self,n,ele=0): #!
        self.ide_ele=ele
        self.num=2**(n-1).bit_length()
        self.seg=[self.ide_ele]*2*self.num
        
    def segfunc(self,x,y): #!
        return math.gcd(x,y)
    
    def init(self,init_val):#初期化
        #set_val
        for i in range(n):
            self.seg[i+self.num-1]=init_val[i]
        #built
        for i in range(self.num-2,-1,-1):
            self.seg[i]=self.segfunc(self.seg[2*i+1],self.seg[2*i+2])
            
    def upgrade(self,k,x):#A[k]をxに変更
        k+=self.num-1
        self.seg[k]=x
        while k:
            k=(k-1)//2
            self.seg[k]=self.segfunc(self.seg[k*2+1],self.seg[k*2+2])
        
    def query(self,p,q):#[p,q)での解答
        if q<=p:
            return self.ide_ele
        p+=self.num-1
        q+=self.num-2
        res=self.ide_ele
        while q-p>1:
            if p&1==0:
                res=self.segfunc(res,self.seg[p])
            if q&1==1:
                res=self.segfunc(res,self.seg[q])
                q-=1
            p=p//2
            q=(q-1)//2
        if p==q:
            res=self.segfunc(res,self.seg[p])
        else:
            res=self.segfunc(self.segfunc(res,self.seg[p]),self.seg[q])
        return res

st=SegmentTree(n,0)
st.init(A)
ans=0
for i in range(n):
  ans=max(ans,math.gcd(st.query(0,i),st.query(i+1,n)))
print(ans)