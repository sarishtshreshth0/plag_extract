n=int(input())
w=list(map(int,input().split()))
s=[0]
for i in w:
    s.append(s[-1]+i)
ss=s[-1]
ans=10**20
for i in range(n+1):
    ans=min(ans,abs((ss-s[i])-s[i]))
print(ans)