import math
n = int(input())
c = [0] * (n-1)
s = [0] * (n-1)
f = [0] * (n-1)
for i in range(n-1):
    cc,ss,ff = map(int,input().split())
    c[i] = cc
    s[i] = ss
    f[i] = ff

ans = [0] * n

for i in range(n-1):
    t = s[i] + c[i]
    for j in range(i+1,n-1):
        if t <= s[j]:
            t = c[j] + s[j]
        else:
            tmp = t - s[j]
            if t % f[j] == 0:
                t +=  c[j]
            else:
                t += f[j] - (t % f[j]) + c[j]
    ans[i] = t
    print(t)
print(0)
