S = input()

ans = 0

def f(i):
  ans = 0
  for c in S:
    if int(c)==i: ans += 1
    i = (i+1)%2
  return ans

ans = min(f(0),f(1))

print(ans)
