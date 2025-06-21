a = input().split()
q = int(a[0]) * 4
h = int(a[1]) * 2
s = int(a[2])
t = int(min([q,h,s]))
d = int(a[3])
b = int(input())

if min([t,d/2]) == t:
  print(int(b * t))
else:
  print(int((b // 2) * d + (b % 2) * t))