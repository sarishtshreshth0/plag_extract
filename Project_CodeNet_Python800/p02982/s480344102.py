import math
n,d = map(int,input().split())
li = []
ans = 0
for i in range(n):
    li.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if i != j:
            a = 0
            b = 0
            for k in range(d):
                a += (li[i][k]-li[j][k])**2
            b = math.sqrt(a)
            if b == int(b):
                ans += 1
print(ans//2)