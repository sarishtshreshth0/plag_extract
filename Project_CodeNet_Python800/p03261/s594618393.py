n = int(input())
x = [input() for i in range(n)]
l = []
foot = x[0][0]
ans = 0
for i in range(len(x)):
  if foot != x[i][0]:
    ans = 1
  foot = x[i][-1]
  if x[i] in l:
    ans = 1
  l.append(x[i])
if ans == 1:
  print('No')
else:
  print('Yes')