N = int(input())

C = []
S = []
F = []
for i in range(N-1):
    c, s, f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)

for i in range(N-1):
    res = S[i] + C[i]
    for j in range(i+1,N-1):
        if res < S[j]:
            res = S[j] + C[j]
        else:
            t = (res - S[j]) % F[j]
            res += (F[j] - t) % F[j] + C[j]
    print(res)

print(0)