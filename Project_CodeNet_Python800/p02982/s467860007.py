import math
n,d = map(int,input().split())
x = [0] * n
ans = 0
for i in range(n):
    x[i] = list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        l = math.sqrt(sum((x[i][f] - x[j][f])**2 for f in range(d)))
        if l%1 == 0:
            ans += 1
print(ans)
