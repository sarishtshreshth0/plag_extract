N,K=list(map(int, input().split()))
ct=0
while N>0:
  N=N//K
  ct+=1
print(ct)