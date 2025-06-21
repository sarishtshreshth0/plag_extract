import numpy as np

N = int(input())
A = list(map(int, input().split()))

S = np.zeros(N+1, dtype='int64') # 累積和
D = {0: 1} # ディクショナリ（連想配列） 各値が何回出てくるか
for i in range(1,N+1): # 1 から N まで
    S[i] = S[i-1] + A[i-1]
    if S[i] in D: D[S[i]] += 1
    else: D[S[i]] = 1

ans = 0
for i in D:
    ans += int(D[i]*(D[i]-1)/2) # 同じ値を2つ選ぶ選び方
print(ans)