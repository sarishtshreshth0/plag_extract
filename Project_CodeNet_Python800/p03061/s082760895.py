from fractions import gcd

def init(init_val):
    for i in range(n):
        seg[i+num-1] = init_val[i]
    for i in range(num-2,-1,-1) :
        seg[i] = gcd(seg[2*i+1],seg[2*i+2]) 

def update(k,x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = gcd(seg[k*2+1],seg[k*2+2])

def query(p,q):
    if q<=p:
        return I
    p += num-1
    q += num-2
    res = I
    while q-p>1:
        if p&1 == 0:
            res = gcd(res,seg[p])
        if q&1 == 1:
            res = gcd(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = gcd(res,seg[p])
    else:
        res = gcd(gcd(res,seg[p]),seg[q])
    return res


I = 0
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
n = int(readline())
a = [int(i) for i in readline().split()]
num = 2**(n-1).bit_length()
seg=[I]*2*num
init(a)
ans = 1
for i in range(n):
  ans = max(ans,gcd(query(0,i),query(i+1,n)))
  
print(ans)