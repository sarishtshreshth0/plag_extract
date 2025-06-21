# Segment Tree
class Segment:
    def __init__(self, N, init_val):
        self.N0 = 2**(N-1).bit_length()
        # 0-indexedで管理
        self.dat = [identity_element]*(2*self.N0)
        # 値を代入
        for i in range(N):
            self.dat[i+self.N0-1]=init_val[i]    
        # 構築
        for i in range(self.N0-2,-1,-1) :
            self.dat[i]=segfunc(self.dat[2*i+1],self.dat[2*i+2]) 

    # k番目の要素の値をxに変更
    def update(self, k, x):
        k += self.N0-1
        self.dat[k] = x
        while k >= 0:
            k = (k-1)//2
            self.dat[k] = segfunc(self.dat[2*k+1], self.dat[2*k+2])

    # 区間[l, r)のsegfuncを求める
    def query(self, l, r):
        L = l + self.N0
        R = r + self.N0
        s = identity_element
        # 区間を列挙しながらsegfuncを求める
        while L < R:
            if R & 1:
                R -= 1
                s = segfunc(s, self.dat[R-1])
            if L & 1:
                s = segfunc(s, self.dat[L-1])
                L += 1
            L >>= 1
            R >>= 1
        return s

# segfunc : min, +, *, xor, gcd
# identity_element : 単位元(min:inf, 和:0, 積:1, xor:0, gcd:0)

from fractions import gcd
def segfunc(x,y):
    return gcd(x,y) # 変える
identity_element = 0 # 変える

n = int(input())
a = list(map(int,input().split()))

h = Segment(n, a)
ans = 0
for i in range(n):
    ans=max(ans,gcd(h.query(0,i), h.query(i+1,n)))
print(ans)
