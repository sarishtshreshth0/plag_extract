n = int(input())
w = [input()]
for i in range(1,n):
  w.append(input())
if len(set(w)) != n:
  print("No")
else:
  for i in range(1,n):
    if w[i-1][-1] != w[i][0]:
      print("No")
      break
  else:
      print("Yes")