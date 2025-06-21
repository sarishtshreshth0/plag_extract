n=int(input())
w=[0]*n
for i in range(n):
  w[i]=input()
if all(len(w)==len(set(w)) and w[i-1][-1]==w[i][0] for i in range(1,n)):
  print("Yes")
else:
  print("No")
