n=int(input())
a=list(map(int,input().split()))
sum_=[a[0]]
num=a[0]
for i in range(1,n):
    num=num+a[i]
    sum_.append(num)
count={}
for i in range(n):
    if sum_[i] in count:
        count[sum_[i]]+=1
    else:
        count[sum_[i]]=1
ans=0
for i in count.values():
    ans+=i*(i-1)//2
if 0 in count:
    ans+=count[0]
print(ans)