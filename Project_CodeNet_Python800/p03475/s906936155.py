N = int(input())
C = []
S = []
F = []
for _ in range(N-1):
    c, s, f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)
for i in range(N):
    if i == N - 1:
        print(0)
        break
    time = 0
    for j in range(i, N-1):
        if time < S[j]:
            time = S[j]
        if time % F[j] == 0:
            time += C[j]
        else:
            time += (F[j] - (time % F[j])) + C[j]
    print(time)
