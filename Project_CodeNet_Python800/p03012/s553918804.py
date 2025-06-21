N = int(input())
W = [int(w) for w in input().split()]
S1 = 0
S2 = 0
ans = []
for i in range(N):
  S2 = sum(W) - S1
  ans.append(abs(S2 - S1))
  S1 = 0
  S2 = 0
  for j in range(i + 1):
    S1 += W[j]
print(min(ans))