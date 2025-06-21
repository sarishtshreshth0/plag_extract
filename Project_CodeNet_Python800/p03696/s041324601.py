n = int(input())
s = input()

l = 0
r = 0
for si in s:
  if si == "(":
    r += 1
  else:
    if r == 0:
      l += 1
    else:
      r -= 1
ans = ""
for _ in range(l):
  ans += "("
ans += s
for _ in range(r):
  ans += ")"
print(ans)

