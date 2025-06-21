
import numpy as np

N = int(input())

Cs = []
Ss = []
Fs = []
ans = [0] * N
ans_fix = [False] * N
for i in range(N-1):
    C,S,F = list(map(int, input().split()))
    Cs.append(C)
    Ss.append(S)
    Fs.append(F)

ans_fix[-1] = True

for i in range(N):
    for j in range(i, N-1):
        if i == 0:
            ans[j] = Ss[j] + Cs[j]
        elif not ans_fix[j-i]:
            if ans[j-i] <= Ss[j]:
                ans[j-i] = Ss[j]
            wait_time = Fs[j] - (ans[j-i] % Fs[j]) if ans[j-i] % Fs[j] != 0 else 0
            ans[j-i] += wait_time + Cs[j]

    ans_fix[N-2-i] = True

for a in ans:
    print(a)