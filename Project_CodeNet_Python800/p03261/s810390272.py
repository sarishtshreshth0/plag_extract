n=int(input())
w=[input() for i in range(n)]
if len(w) != len(set(w)):
  print("No")
  exit()
for i in range(n -1):
  if w[i][-1] != w[i+1][0]:
    print("No")
    exit()
print("Yes")