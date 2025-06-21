n,k = map(int,input().split())
a = []
if n//k == 0:
  print(1)

else:
  while n//k != 0:
    a.append(n%k)
    n = n//k
  
    if n//k ==0:
      a.append(n%k)
  a.reverse()
  
  print(len(a))