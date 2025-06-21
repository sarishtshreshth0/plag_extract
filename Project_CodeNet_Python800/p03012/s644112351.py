N = int(input())
W = list(map(int, input().split()))
S = []
s = 0
for i in range(N):
  s += W[i]
  S.append(s)
print(min([abs(S[N-1] - 2 * S[i]) for i in range(N)]))