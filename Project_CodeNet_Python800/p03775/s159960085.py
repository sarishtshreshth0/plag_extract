n = int(input())
#n, m = map(int, input().split())
#xl = list(map(int, input().split()))
#al=[list(input()) for i in range(n)]
a=1
ans=len(str(n))
while a**2<=n:
    if n%a==0:
        b=n//a
        ans=min(ans, max(len(str(a)),len(str(b))))
    a+=1
print(ans)