S=input()
T="YAKI"
ans=1
if(len(S)<4):
  ans=0
else:
  for i in range(4):
    if(S[i]!=T[i]):
      ans=0
if(ans):
  print("Yes")
else:
  print("No")