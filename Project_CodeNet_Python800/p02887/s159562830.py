n = int(input())
S = input()

res = 1
tmp = S[0]
for i in range(1,n):
  if S[i] != tmp:
    res += 1
  tmp = S[i]
print(res)
