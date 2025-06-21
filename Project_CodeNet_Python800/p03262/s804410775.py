N,X = map(int,input().split())
x = list(map(int,input().split()))
x.append(X)
x.sort()
Mindif = x[1]-x[0]
import math
for i in range(1,N):
    Mindif = math.gcd(Mindif,x[i+1]-x[i])
print(Mindif)