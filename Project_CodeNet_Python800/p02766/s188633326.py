N,K=input().split()
N=int(N)
K=int(K)
n=0
i=1
while i<=N:
  n=n+1
  i=K**n
print(n)