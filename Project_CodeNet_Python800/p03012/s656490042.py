n = int(input())
w = list(map(int, input().split()))

a = [0]*(n+1)
j = 0

for i in range(n):
  a[0] += w[i]

for i in range(n+1):
  if a[i] > 0:
    a[i+1] = a[i]- 2*w[i]
  else:
    j = i
    break
    
p = -a[j]
q = a[j-1]
if p < q:
  print(p)
else:
  print(q)




