q,h,s,d = map(int,input().split())
n = int(input())

ans = 0
#2Lの一番良い買い方をする
if n>=2:
    amount = n//2
    n-=amount*2
    ans+=min(q*8,h*4,s*2,d*1)*amount
if n==1:
    ans+=min(q*4,h*2,s*1)
print(ans)