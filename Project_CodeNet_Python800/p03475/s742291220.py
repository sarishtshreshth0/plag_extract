N = int(input())
C = [0]
S = [0]
F = [0]
for i in range(N - 1):
    c, s, f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)

for i in range(1, N):
    t = 0
    for j in range(i, N):
        if j == i:
            t += S[j]
        if t >= S[j]:
            if t % F[j] != 0:
                t += F[j] - (t % F[j])
            t += C[j]
        else:
            t = S[j] + C[j]
    print(t)
print(0)
