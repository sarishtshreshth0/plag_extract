N, A, B = map(int, input().split())

S = input()

total = 0
abroad = 0

for s in S:
  if s == 'a' and total < (A+B):
    print('Yes')
    total += 1
  elif s == 'b' and total < (A+B) and abroad < B:
    print('Yes')
    total += 1
    abroad += 1
  else:
    print('No')