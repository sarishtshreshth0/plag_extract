import bisect
import math
n = int(input())
a = list(map(int,input().split()))

s = [0]*(n+1)

for i,e in enumerate(a):
    s[i+1] = s[i] + e

def comb(n,m):
    return math.factorial(n)//math.factorial(m)//math.factorial(n-m)

ans = 0
s = sorted(s)

l = 0
r = 0
#print(s)
while l < n+1:
    while r < n+1  and s[l] == s[r]:
        #print(r,s[r])
        r += 1

    if r-l >= 2:
        ans += comb(r-l,2)
    l = r

print(ans)
