N = int(input())
w = []
for i in range(N):
  w.append(input())

v = True
z = list(set(w))
if len(z) != len(w):
  print("No")
else:
  for j in range(N - 1):
    if w[j][-1] != w[j+1][0]:
      v = False
  print("Yes") if v else print("No")
