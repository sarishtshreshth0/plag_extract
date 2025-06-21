n=int(input())
a=list(map(int,input().split()))
num=[0]
num1=0
for i in range(n):
    num1+=a[i]
    num.append(num1)
num.sort()
num2=[]
cnt=0
num3=num[0]
for i in range(1,n+1):
    if num3!=num[i]:
        if cnt!=0:
            num2.append(cnt)
        num3=num[i]
        cnt=0
    else:
        cnt+=1
if cnt!=0:
    num2.append(cnt)
ans=0
for i in range(len(num2)):
    ans+=((num2[i]+1)*num2[i])//2
print(ans)
