A,B = map(int,input().split())
S = str(input())
for i in range(len(S)):
  if i < A:
    if not S[i].isnumeric():
      print("No")
      exit()
  elif i == A:
    if S[i] != "-":
      print("No")
      exit()
  else:
    if not S[i].isnumeric():
      print("No")
      exit()
print("Yes")