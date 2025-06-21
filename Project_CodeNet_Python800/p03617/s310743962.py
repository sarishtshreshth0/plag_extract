Q, H, S, D = map(int, input().split())
N = int(input())

p025 = Q
p05 = min(H, p025 * 2)
p1 = min(S, p05 * 2)
p2 = min(D, p1 * 2)

ans = 0
if N % 2 != 0:
    N -= 1
    ans += p1
ans += (N // 2) * p2

print(ans)
