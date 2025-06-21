n,k=map(int,input().split())
d=[]
while n>0:
    d.append(str(n%2))
    n=n//k
print(len(d))