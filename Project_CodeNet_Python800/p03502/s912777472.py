N = input()
X = int(N)
l = [int(i) for i in list(N)]
f = sum(l)
if X % f == 0:
  print("Yes")
else:
  print("No")