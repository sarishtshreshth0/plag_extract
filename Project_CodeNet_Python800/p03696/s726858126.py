N = int(input())
S = list(input())

a = 0 # (
b = 0 # )
for i in range(N):
  if S[i] == '(':
    a += 1
  else:
    if a > 0:
      a -= 1
    else:
      b += 1

ans = "".join(S)
if b > 0:
  ans = "("*b + ans
if a > 0:
  ans = ans + ")"*a
print(ans)
