A, B = map(int, input().split())
S = input()
if S[:A].isdecimal() and S[A+1:].isdecimal() and S[A] == '-':
  print("Yes")
else:
  print("No")
