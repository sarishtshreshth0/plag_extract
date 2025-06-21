n = int(input())

cand = []
def rec(n):
  if n > 10**9:
    return
  cand.append(n)
  rec(int(str(n) + "3"))
  rec(int(str(n) + "5"))
  rec(int(str(n) + "7"))
rec(3)
rec(5)
rec(7)
ans = 0

def check(c):
  if "3" in str(c) and "5" in str(c) and "7" in str(c):
    return True
  else:
    return False

for c in cand:
  if c <= n and check(c):
    ans += 1
print(ans)