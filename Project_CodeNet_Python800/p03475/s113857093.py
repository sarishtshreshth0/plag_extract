def ceil(n, m):
    return -(-n // m)

N = int(input())
C, S, F = zip(*[[int(x) for x in input().split()] for _ in range(N - 1)])

t = [0] * N
for i in range(N - 1):
    # 駅iから出発する人
    for j in range(i, N - 1):
        t[i] = F[j] * ceil(t[i], F[j])  # 駅jから出発する時刻（S[j]=0の場合）
        t[i] = max(S[j], t[i]) # 駅jから出発する時刻
        t[i] = t[i] + C[j] # 駅j+1に到着する時刻

for i in range(N):
    print(t[i])