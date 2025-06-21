n = int(input())
w = list(map(int,input().split()))
s = sum(w)
ans = 10**5
f = 0
for i in range(n):
    f += w[i]
    if abs(f-(s-f)) < ans:
        ans = abs(f-(s-f))
print(ans)