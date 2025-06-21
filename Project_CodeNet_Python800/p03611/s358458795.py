n=int(input())
A=list(map(int,input().split()))
Alist=[0]*(10**5+1)
for a in A:
    Alist[a]+=1
ans=1
for i in range(min(A),max(A)):
    ans=max(ans,Alist[i]+Alist[i+1]+Alist[i+2])
if min(A)==max(A):
    ans=n
print(ans)