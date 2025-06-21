n=int(input())
w=list(map(int,input().split()))
ans=100000
for i in range(1,len(w)):
    if abs(sum(w[i:])-sum(w[:i]))<ans:
        ans=abs(sum(w[i:])-sum(w[:i]))
print(ans)