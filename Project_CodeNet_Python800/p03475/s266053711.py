def solve(k):
    t = 0
    for i in range(k, N-1):
        if t < S[i]:
            t = S[i] + C[i]
        else:
            if (t - S[i]) % F[i] == 0:
                t += C[i]
            else:
                t = t + (F[i] - (t - S[i]) % F[i]) + C[i]
    return t

N = int(input())
C, S, F = [0] * (N - 1), [0] * (N - 1), [0] * (N - 1)
for i in range(N-1):
    C[i], S[i], F[i] = map(int, input().split())
res = [0] * N
for i in range(N):
    res[i] = solve(i)
print(*res, sep='\n')
