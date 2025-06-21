n=int(input())
csf=[list(map(int,input().split())) for _ in range(n-1)]
for i in range(n-1):
    ans=0
    for j in range(i,n-1):
        c = csf[j][0]
        s = csf[j][1]
        f = csf[j][2]
        if j==i:
            ans+=s+c
        else:
            if ans<s:
                ans=s+c
            else:
                ans+=(f-(ans-s)%f)%f+c
    print(ans)
print(0)