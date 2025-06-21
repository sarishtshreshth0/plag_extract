A,B = map(int,input().split())
S = input()

if len(S)==A+B+1 and S[A]=="-" and S.count("-")==1:
  print("Yes")
else:
  print("No")