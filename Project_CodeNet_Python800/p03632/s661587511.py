i = list(map(int, input().split()))

A=i[0]
B=i[1]
C=i[2]
D=i[3]

if(C-B>=0 or A-D>=0):
  print(0)
else:
  print(min(B,D) - max(A,C))