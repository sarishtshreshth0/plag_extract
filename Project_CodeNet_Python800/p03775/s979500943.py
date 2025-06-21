n=int(input())

ans=20
for i in range(1, int(n**0.5)+1):
    if n%i==0:
        j=n//i
        x=max(len(str(i)),len(str(j)))
        ans=min(ans,x)
print(ans)