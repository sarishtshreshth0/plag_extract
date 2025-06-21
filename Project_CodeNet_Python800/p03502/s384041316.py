N = input()
f = 0

for n in N:
  f+=int(n)
  
if int(N) % f==0:
  print("Yes")
else:
  print("No")