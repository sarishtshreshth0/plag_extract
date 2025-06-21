n=int(input())
w=list(map(int,input().split()))
S=sum(w)
ans=10000
for i in range(n-1):
    s1=0
    s2=0
    for p in range(i+1):
        s1+=w[p]
    for q in range(i+1,n):
        s2+=w[q]
    if abs(s1-s2)<ans:
        ans=abs(s1-s2)
print(ans)