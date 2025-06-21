import sys
# from math import gcd
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
pref,suf = [0]*(n+2),[0]*(n+2)
pref[1] = a[0]
for i in range(2,n+1):
    pref[i] = gcd(pref[i-1],a[i-1])
suf[n] = a[n-1]
for i in range(n-1,0,-1):
    suf[i] = gcd(suf[i+1],a[i-1])
ans = max(suf[2],pref[n-1])
for i in range(2,n):
    ans = max(ans,gcd(pref[i-1],suf[i+1]))
print(ans)
