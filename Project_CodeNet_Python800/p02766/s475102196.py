N,K=map(int,input().split())
num=0
while N>=K:
    N=N//K
    num+=1
print(num+1)