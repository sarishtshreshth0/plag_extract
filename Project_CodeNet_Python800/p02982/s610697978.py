n, d = map(int, input().split())
ar = []
count = 0
for i in range(n):
  ar.append(list(map(int, input().split())))
  
for i in range(n):
  for j in range(n):
    s = 0
    if i == j:
      break
    else:
      for k in range(d):
        s += (ar[i][k] - ar[j][k])**2
      f = s**(1/2)
      if f.is_integer(): 
        count +=1
print(count)