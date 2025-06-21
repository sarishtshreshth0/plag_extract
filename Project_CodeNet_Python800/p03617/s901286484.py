q, h, s, d = map(int, input().split())
n = int(input())
l = [4 * q, 2 * h, s, d / 2]
ans = 0
if n >= 2:
  a = l.index(min(l))
  if a == 0:
    ans = 4 * q * n
  elif a == 1:
    ans = 2 * h * n
  elif a == 2:
    ans = s * n
  elif a == 3:
    if n % 2 == 0:
      ans = n // 2 * d
    elif n % 2 == 1:
      ans = n // 2 * d
      b = l.index(min(l[:3]))
      if b == 0:
        ans += 4 * q
      elif b == 1:
        ans += 2 * h
      elif b == 2:
        ans += s
else:
  b = l.index(min(l[:3]))
  if b == 0:
    ans = 4 * q * n
  elif b == 1:
    ans = 2 * h * n
  elif b == 2:
    ans = s * n
print(ans)
