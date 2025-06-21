N, K = map(int, input().split())
q, r = divmod(N, K)
ans = 1
while q > 0:
    q, r = divmod(q, K)
    ans += 1
print(ans)
