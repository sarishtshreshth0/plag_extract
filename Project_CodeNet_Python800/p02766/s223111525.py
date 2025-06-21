n,k=map(int,input().split())
result=''
while n>=1:
    b=n%k
    result+=str(b)
    n//=k
print(len(result))
