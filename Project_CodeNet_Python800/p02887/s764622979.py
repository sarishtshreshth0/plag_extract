N = int(input())
S = list(input())
ans = [S[0]]
for i in range(1, N):
  if S[i-1] != S[i]:
    ans.append(S[i])
print(len(ans))