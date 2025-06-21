N,A,B = map(int,input().split())
S = input()

countA = 0
countB = 0

for i in range(len(S)):
  if S[i] == 'a':
    if countA+countB < A+B:
      countA += 1
      print("Yes")
    else:
      print("No")
    
  elif S[i] == 'b':
    if countA+countB < A+B and countB < B:
      countB += 1
      print("Yes")
    else:
      print("No")
    
  elif S[i] == 'c':
    print("No")