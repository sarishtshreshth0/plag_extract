Q, H, S, D = map(int, input().split())
N = int(input())

H = min(H, 2 * Q)
S = min(S, 2 * H)

res = 0
if 2 * S <= D:
	res = N * S
elif 2 * S > D:
	if N % 2 == 0:
		res = D * (N // 2)
	else:
		res = D * (N // 2) + S

print(res)