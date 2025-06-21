q,h,s,d=map(int,input().split())
n=int(input())
num1=n%2
num2=n//2
num10=min(q*4,h*2,s)
num20=min(q*8,h*4,s*2,d)
ans=0
if num1==1:
    ans+=num10
ans+=num2*num20
print(ans)
