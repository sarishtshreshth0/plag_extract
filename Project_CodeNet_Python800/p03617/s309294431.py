Q, H, S, D = map(int, input().split())
N = int(input())

nQ = 4 * Q
nH = 2 * H
nS = S
nD = D / 2

if nD < min(nQ, nH, nS):
    ans = D * (N // 2) + min(nQ, nH, nS) * (N - (N // 2) * 2)
else:
    ans = min(nQ, nH, nS) * N
print(ans)
