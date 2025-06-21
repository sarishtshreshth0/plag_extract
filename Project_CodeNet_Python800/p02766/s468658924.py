N,K=map(int,input().split())
a=0
while N>0:
    a+=1
    N=N//K
print(a)