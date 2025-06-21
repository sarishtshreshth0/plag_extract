n = int(input())
csf = []
for i in range(n-1):
    t = list(map(int, input().split()))
    csf.append(t)

ans = []
for i in range(n-1):
    now = 0
    for c,s,f in csf[i:]:
        if now < s:
            now = s
        now += (s-now)%f+c
    ans.append(now)
ans.append(0)

for a in ans:
    print(a)