n = int(input())
a = list(map(int, input().split()))

sa = [0 for _ in range(n+1)]
for i in range(n):
    sa[i+1] = sa[i] + a[i]

sa.sort()
ans = 0
tmp = - 10 ** 10
cnt = 1
for i in range(n+1):
    if sa[i] == tmp:
        cnt += 1
    else:
        ans += cnt * (cnt - 1) // 2
        tmp = sa[i]
        cnt = 1

ans += cnt * (cnt - 1) // 2

print(ans)