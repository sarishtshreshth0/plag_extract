n,c = map(int,input().split())
x = [c] + list(map(int,input().split()))
x.sort()
ans = x[1]-x[0]
import math
for i in range(1,n):
    ans = math.gcd(ans,x[i+1]-x[i])
print(ans)