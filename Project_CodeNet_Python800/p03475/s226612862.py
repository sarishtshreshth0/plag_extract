N = int(input())
from math import floor
C, S, F = [], [], []
for _ in range(N-1):
    c, s, f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)

for start in range(N):
    ans = 0
    if start == N-1:
        print(ans)
        break
    for i in range(start, N-1):
        if ans <= S[i]:
            ans = S[i]
            ans += C[i]
        else:
            if ans % F[i] == 0:
                ans += C[i]
            else:
                ans += (F[i] - ans % F[i])
                ans += C[i]
            
    print(ans)