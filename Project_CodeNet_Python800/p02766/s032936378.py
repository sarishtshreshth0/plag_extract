N,K=input().split()
N=int(N)
K=int(K)
count=0
while N>0:
  count=count+1
  N=N//K
  
print(count)