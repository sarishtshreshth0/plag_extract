N = int(input())
W = []
flag = 1

for i in range(N):
  w = input()
  W.append(w)
  
  if i != 0:
    if W[i-1][-1] != W[i][0] or W.count(w) >= 2:
      flag = 0
      
if flag:
  print("Yes")
else:
  print("No")