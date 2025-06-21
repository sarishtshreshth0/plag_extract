n, d = map(int, input().split())
x=[]
for i in range(n):
    x.append([int(x) for x in input().split()])

from math import sqrt
ans=0

for i in range(n-1):
    for j in range(i+1,n):
        forsq=0
        for k in range(d):
            forsq += (x[i][k] - x[j][k])**2
        a = (sqrt(forsq))
        if a.is_integer():
            ans+=1

print(ans)