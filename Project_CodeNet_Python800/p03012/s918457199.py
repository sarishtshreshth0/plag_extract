from itertools import accumulate
n=int(input())
w=list(map(int,input().split()))
tmp=0
l=list(accumulate(w))
ans=float("inf")
for i in range(n):
    tmp=abs(l[i]-(l[n-1]-l[i]))
    if tmp<ans:
        ans=tmp
print(ans)