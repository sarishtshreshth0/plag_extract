N = int(input())
CSF = [map(int, input().split()) for _ in range(N-1)]
C, S, F = [list(i) for i in zip(*CSF)]

for i in range(N):
    if i == N-1:
        print(0)
    else:
        t = S[i]
        for j in range(N-i-1):
            t = max(((t+F[i+j]-1)//F[i+j])*F[i+j], S[i+j])+C[i+j]
        print(t)