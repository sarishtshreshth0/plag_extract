N, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)

li = []
x.sort()
for i in range(N):
  li.append(x[i+1]-x[i])
  
li.sort()
while len(li) > 1:
  l = []
  div = li[0]
  for n in li:
    mod = n % div
    if mod != 0:
      l.append(mod)
  l.append(div)
  l.sort()
  li = l
print(*li)