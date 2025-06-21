l = [int(i) for i in input().split()]
l_sorted = sorted(l)
if l[2] == l_sorted[1]:
  print('Yes')
else:
  print('No')