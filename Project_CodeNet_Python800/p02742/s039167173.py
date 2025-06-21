h, w = [int(i) for i in input().split()]

if h == 1 or w == 1:
  print(1)
  exit(0)

s = h * w
if s % 2 == 0:
  print(s // 2)
  exit(0)
print(s // 2 + 1)
