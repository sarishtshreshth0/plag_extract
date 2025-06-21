import math

n=int(input())
for i in range(1,int(math.sqrt(n))+1):
    ans=0
    if n%i==0:
        j=int(n/i)
        ans1=str(i)
        ans2=str(j)
        if len(ans1)>=len(ans2):
            break

if len(ans1)>=len(ans2):
    print(len(ans1))
else:
    print(len(ans2))