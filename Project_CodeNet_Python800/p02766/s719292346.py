N, K = [int(_) for _ in input().split()]
ans = 0
while N:
    N //= K
    ans += 1
print(ans)
