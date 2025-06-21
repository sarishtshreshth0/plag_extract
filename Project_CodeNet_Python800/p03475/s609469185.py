N = int(input())
C = [0] * (N - 1)
S = [0] * (N - 1)
F = [0] * (N - 1)
for i in range(N-1):
    c, s, f = map(int, input().split())
    C[i] = c
    S[i] = s
    F[i] = f
for i in range(N-1):
    ttl = 0
    for j in range(i, N-1):
        if ttl < S[j]:
            ttl = C[j] + S[j]
        elif ttl % F[j] == 0:
            ttl += C[j]
        else:
            ttl += F[j] - (ttl % F[j]) + C[j]
    print(ttl)
print(0)