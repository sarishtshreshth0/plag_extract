import sys
n=int(input())
w=[]
for i in range(n):
  w.append(input())

if len(w)!=len(set(w)):
  print('No')
  sys.exit()

for i in range(n-1):
  p=list(w[i])
  q=list(w[i+1])
  if p[-1]!=q[0]:
    print('No')
    sys.exit()
  
print('Yes')