import math
N,X =list(map(int,input().split()))
x =list(map(int,input().split()))
lis_x = []
for i in range(N):
    lis_x.append(abs(x[i]-X))
ans = lis_x[0]
for i in range(1,N):
    ans = math.gcd(ans,lis_x[i])
print(ans)
