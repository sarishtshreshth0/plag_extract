A,B=map(int,input().split())
S=input()
if "0"<=S[0:A] and S[0:A]<="9"*A:
  if S[A:A+1]=="-" :
    if "0"<=S[A+1:A+B+1] and S[A+1:A+B+1]<="9"*B :
      print("Yes")
      exit()
print("No")