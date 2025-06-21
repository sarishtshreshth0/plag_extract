N = int(input())
memo = [0]*N
C = [0]*N
S = [0]*N
F = [0]*N



for i in range(N-1):
    Ci, Si, Fi = map(int, input().split())
    C[i], S[i], F[i] = Ci, Si, Fi

for i in range(N):
    t = 0
    for j in range(i, N-1):
        if t < S[j]:
            t = S[j]
        else:
            if t % F[j] == 0:
                pass
            else:
                t = t+F[j]-(t%F[j])
        t += C[j]

    print(t)
