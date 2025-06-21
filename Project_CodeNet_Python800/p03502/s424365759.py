N = input()
Nnum = int(N)
Nls = list(N)
Nls = [int(i) for i in Nls]
FN = sum(Nls)
if Nnum%FN == 0:
  print('Yes')
else:
  print('No')