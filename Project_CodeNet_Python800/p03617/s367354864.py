Q, H, S, D = map(int, input().split())
N = int(input())

D = min(8 * Q, 4 * H, 2 * S, D)
S = min(4 * Q, 2 * H, S)
ans = (N // 2) * D + (N % 2) * S
print(ans)