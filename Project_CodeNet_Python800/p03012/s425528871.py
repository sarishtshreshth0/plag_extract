N = int(input())
W = list(map(int, input().split()))
S = [0]
for i in range(N):
  S.append(S[i] + W[i])
ans = float("inf")
for j in range(N):
  ans = min(abs(S[-1] - 2*S[j]), ans)
print(ans)