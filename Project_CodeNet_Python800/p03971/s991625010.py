N, A, B = map(int, input().split())
S = input()
all = 0
foreign = 0

for i in range(len(S)):
  if S[i] == 'a' and all < A + B:
    print('Yes')
    all += 1
    continue
  if S[i] == 'b' and all < A + B and foreign < B:
    print('Yes')
    all += 1
    foreign += 1
    continue
  print('No')