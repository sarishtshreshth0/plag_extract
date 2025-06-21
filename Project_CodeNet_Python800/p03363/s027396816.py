N=int(input())
A=list(map(int,input().split()))
import copy
li=[0]
ans=0

for j in range(N):
    ans+=A[j]
    li.append(copy.copy(ans))

li.sort()
ans=0
temp=1
for i in range(N):

    if li[i]==li[i+1]:
        temp+=1
    else:
        ans+=temp*(temp-1)//2
        temp=1
ans+=temp*(temp-1)//2
print(ans)
