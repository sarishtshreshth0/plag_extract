n,k=map(int,input().split())
a=0
b=n
while b>=k:

    b=b//k

    a+=1

print(a+1)
