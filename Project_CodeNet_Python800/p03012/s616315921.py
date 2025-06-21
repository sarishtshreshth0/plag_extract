n=int(input())
l=list(map(int,input().split()))
l_sum=sum(l)
ans=l_sum
c1=0
c2=0

for i in range(len(l)):
    c1=l_sum-sum(l[:i+1])
    c2=abs(c1-sum(l[:i+1]))

    if ans> c2:
        ans=c2
  
print(ans)