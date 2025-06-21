N = int(input())
A = list(map(int,input().split()))
lis = [0] * (N+1)
for i in range(N):
    lis[i+1] = lis[i] + A[i]
d = {}
for i in lis:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
ans = 0
for i in d:
    if d[i] > 1:
        ans += (d[i] * (d[i]-1)) // 2
print(ans)
