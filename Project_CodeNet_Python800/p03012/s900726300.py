n=int(input())
w=list(map(int, input().split()))

ans=10**10

for t in range(1,n):
    ans=min(ans,abs(sum(w[0:t])-sum(w[t:])))
print(ans)