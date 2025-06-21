Q, H, S, D = map(int, input().split())
N = int(input())

min_1l = min([4 * Q, 2 * H, 1 * S])
min_2l = min([8 * Q, 4 * H, 2 * S, D])

ans = 0
if min_2l == D:
  ans = D * (N // 2) + (N % 2) * min_1l
else:
  ans = N * min_1l

print(ans)
