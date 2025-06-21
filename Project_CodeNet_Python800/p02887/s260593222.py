N = int(input())
S = input()

ans = 1
for i, s in enumerate(S):
  if i == N-1:
    break
  if s == S[i+1]:
    continue
  else:
    ans += 1

print(ans)