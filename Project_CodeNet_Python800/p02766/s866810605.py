N,K=map(int,input().split())
n=1
while 1:
  if N<K**n:break
  n+=1
print(n)