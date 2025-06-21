n=int(input())
w=list(map(int,input().split()))
ans=10**5
for i in range(n-1):
    s1=0
    s2=0
    for a in range(i+1):
        s1+=w[a]
    for b in range(i+1,n):
        s2+=w[b]
    if abs(s1-s2)<ans:
        ans=abs(s1-s2)
print(ans)