A,B = map(int,input().split())
S = list(input())

ok = True
for i in range(A+B+1):
  s = S[i]
  if i == A and s != '-':
    ok = False
    break
  
  if i != A and s == '-':
    ok = False
    break
    
if ok:
  print("Yes")
else:
  print("No")
    
  
