A,B=map(int,input().split())
S=input()
if S[A]=="-":
  for i in range(A):
    if S[i]=="-":
      print("No")
      break
  else:
    for j in range(B):
      if S[-j-1]=="-":
        print("No")
        break
    else:
      print("Yes")
else:
  print("No")