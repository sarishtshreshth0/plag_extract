import sys

n = int(input())
l = [input() for i in range(n)]
for i in range(n):
  if i > 0:
    if l[i-1][-1] != l[i][0]:
      print("No")
      sys.exit()
  if l.count(l[i]) > 1:
    print("No")
    sys.exit()
print("Yes")