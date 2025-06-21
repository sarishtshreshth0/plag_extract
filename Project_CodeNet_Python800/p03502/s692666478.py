f=0
n=int(input())
s=n
for i in range(len(str(n))):
  f += (s % 10)
  s = int(s/10)
if n % f == 0:
  print('Yes')
else:
  print('No')