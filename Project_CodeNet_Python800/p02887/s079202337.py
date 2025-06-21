N = int(input())
S = input()
a = S[0]
ans = 1
for i in range(N-1):
  if a != S[i+1]:
    ans += 1
  a = S[i+1]
print(ans)