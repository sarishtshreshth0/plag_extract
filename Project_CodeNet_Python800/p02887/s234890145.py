N = int(input())
S = input()
tmp = S[0]
ans = 1
for n in range(1,N):
  if S[n] != tmp:
    ans += 1
    tmp = S[n]
print(ans)