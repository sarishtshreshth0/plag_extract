N = int(input())
W = [input() for i in range(N)]

l = []

for i in range(N):
  if i != 0:
    if W[i-1][-1] != W[i][0]:
      print('No')
      break
  
  if W[i] in l:
    print('No')
    break
    
  l.append(W[i])
else:
  print('Yes')