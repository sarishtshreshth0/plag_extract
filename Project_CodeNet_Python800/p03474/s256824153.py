A,B = map(int,input().split())
S = input()
flag = False

if S[A] == "-" and S[0:A].isdecimal() and S[A+1:A+B+1].isdecimal():
  flag = True

if flag:
  print("Yes")
else:
  print("No")