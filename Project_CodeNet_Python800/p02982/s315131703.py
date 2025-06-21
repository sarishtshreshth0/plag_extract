from math import sqrt
n,d = map(int,input().split())
x = [list(map(int,input().split())) for i in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1,n):
        t = 0
        for k in range(d):
            t += (x[i][k] - x[j][k]) ** 2
        if float.is_integer(sqrt(t)):
            ans += 1
print(ans)