S = input()
N = int(S)
fN = sum([int(si) for si in S])
if N%fN == 0:
  print('Yes')
else:
  print('No')
