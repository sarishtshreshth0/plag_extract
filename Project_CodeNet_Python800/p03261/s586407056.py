n = int(input())
w= [input() for i in range (n)]
if len(set(w)) == n and all (w[i][-1] == w[i + 1][0] for i in range (n - 1) ):
  print("Yes")
else:
  print("No")

