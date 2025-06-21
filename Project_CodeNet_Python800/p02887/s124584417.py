N = int(input())
S = list(input())

cnt = 1
tmp = S[0]
for k in range(1, N):
  if not S[k] == tmp:
    cnt += 1
  tmp = S[k]
print(cnt)