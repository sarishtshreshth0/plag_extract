n=int(input())
d=input()
ans=""
for i in range(n-1):
    if d[i]!=d[i+1]:
        ans+=d[i]
if d[n-1]!=ans[:-1]:
    ans+=d[n-1]

print(len(ans))
