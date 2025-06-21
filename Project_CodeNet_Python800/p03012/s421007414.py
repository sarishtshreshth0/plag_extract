n=int(input())
w=list(map(int,input().split()))
s=[w[0]]
sum=sum(w)
ans=sum
for i in range(1,n):
    temp=s[i-1]+w[i]
    s.append(temp)
    ans=min(ans,abs(sum-2*s[i]))
print(ans)