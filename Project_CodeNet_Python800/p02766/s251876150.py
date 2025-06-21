N,R=map(int,input().split())
num=0
while N>=R:
    N=N/R
    num+=1
print(num if N==0 else num+1)