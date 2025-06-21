n,k=map(int,input().split())
x,i=0,0
while n>0:
    x+=(n%k)*10**i
    n=n//k
    i+=1
print(len(str(x)))