n = int(input())
w = [input() for _ in range(n)]

t = w[0][-1]
for i in range(1,n):
  if w[i][0] != t:
    print("No")
    break
  t = w[i][-1]
else:
  if n == len(set(w)): print("Yes")
  else: print("No")