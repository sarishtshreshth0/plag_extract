a,b =map(int,input().split())
A,B,C =("Alice","Bob","Draw")
if max(a,b) ==13 and min(a,b) ==1:
  print(A) if a < b else print(B)
else:
  if a > b:
    print(A)  
  elif a < b:
    print(B)  
  else:
    print(C)