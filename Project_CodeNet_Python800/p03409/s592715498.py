n=int(input())
R=[list(map(int,input().split())) for i in range(n)]
B=sorted([list(map(int,input().split())) for i in range(n)])
a=0
for i in range(n):
  y=-1
  c=-1
  for j in range(n-a):
    if R[j][0]<B[i][0] and R[j][1]<B[i][1]:
      if R[j][1]>y:
        y=R[j][1]
        c=j
  if c==-1:
    continue
  else:
    R.pop(c)
    a=a+1
print(a)