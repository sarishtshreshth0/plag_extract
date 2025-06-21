n = int(input())
ws = [str(input()) for i in range(n)]
t = ws[0][0]
for w in ws:
  if ws.count(w) > 1:
    print('No')
    break
  if t[-1] != w[0]:
    print('No')
    break
  else:
    t = w
    n-=1
if n == 0:
  print('Yes')