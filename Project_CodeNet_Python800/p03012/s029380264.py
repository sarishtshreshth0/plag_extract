n=int(input())
w=list(map(int,input().split()))
t=1
ans=sum(w)
for i in range(n):
    s1=w[i:]
    s2=w[:i]
    s=abs(sum(s1)-sum(s2))
    if s<ans:
        ans=s
print(ans)
