a,b=map(int,input().split())
res = 1
for i in range(100):
  if b**i > a:
    res = i
    break
print(res)