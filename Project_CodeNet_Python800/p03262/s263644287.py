from math import gcd
n,X = map(int,input().split())
x = list(map(int,input().split())) + [X]
d = [abs(x[i]-x[i+1]) for i in range(n)]
ans = 0
for i in d:
    ans = gcd(ans,i)
print(ans)