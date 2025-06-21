import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


q,h,s,d = list(map(int, input().split()))
n = int(input())
vals = [q*4, h*2, s, d/2]
v = min(vals)
if v==q*4:
    ans = n*4*q
elif v==h*2:
    ans = n*2*h
elif v==s:
    ans = n*s
else:
    ans = (n//2)*d
    vv = min(vals[:-1])
    if n%2!=0:
        ans += vv
print(ans)