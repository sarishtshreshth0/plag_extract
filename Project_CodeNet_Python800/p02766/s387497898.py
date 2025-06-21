N,K=map(int,input().split())
result=0
for i in range(10**9):
  if (N<K**i):
    result+=i
    break
print(result)