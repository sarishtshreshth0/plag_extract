q, h, s, d = (int(x) for x in input().split())
n = int(input())
l1 = min(4*q, 2*h, s)
l2 = min(8*q, 4*h, 2*s, d)
if n%2 == 0:
  print((n//2) * l2)
else:
  print((n//2) * l2 + l1)