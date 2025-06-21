x = int(input())
f = 0
for s in str(x):
  f += int(s)
if x%f==0:
  print("Yes")
else:
  print("No")