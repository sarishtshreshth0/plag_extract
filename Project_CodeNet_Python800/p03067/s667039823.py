inp = input().split(' ')
a = [int(s) for s in inp]
mi = min(a[:2])
ma = max(a[:2])
if mi <= a[2] <= ma:
  print('Yes')
else:
  print('No')