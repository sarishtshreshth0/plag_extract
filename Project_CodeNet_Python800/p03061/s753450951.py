import math

MAXN = 2 ** 17

ide_ele = 0

n = int(input())
a = list(map(int,input().split()))

num = 2**(n-1).bit_length()
seg = [ide_ele] * 2 * num

def init(init_val):
    for i in range(n):
        seg[i+num-1] = init_val[i]
    for i in range(num-2 ,-1, -1) :
        seg[i] = math.gcd(seg[2*i+1],seg[2*i+2])
        
def update(k,x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = math.gcd(seg[k*2+1] , seg[k*2+2])

init(a)
ans = 0
for i in range(n):
    update(i,0)
    ans = max(ans,seg[0])
    update(i,a[i])
    
print(ans)