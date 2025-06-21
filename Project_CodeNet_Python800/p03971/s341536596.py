N,A,B = map(int,input().split())
S = input()
countA = 0
countB = 0

for i in range(len(S)):
  if S[i] == 'a' and countA + countB < A + B:
    countA += 1
    print('Yes')
  elif S[i] == 'b' and countA + countB < A + B and countB < B:
    countB += 1
    print('Yes')
  else:
    print('No')