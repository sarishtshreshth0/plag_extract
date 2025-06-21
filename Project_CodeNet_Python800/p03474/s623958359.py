A, B = input().split(" ")
S = input()

if S[int(A)] == '-' and S[:int(A)].isdecimal() and S[int(A)+1:int(A)+int(B)+1].isdecimal():
  print("Yes")
else:
  print("No")