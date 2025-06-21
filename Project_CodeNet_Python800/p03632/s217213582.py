A, B, C, D = map(int, input().split())
T = max(B, D) + 1
ans = 0
for i in range(T):
    if A <= i < B and C <= i < D:
        ans += 1

print(ans)
