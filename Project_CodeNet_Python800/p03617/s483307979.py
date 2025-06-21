q,h,s,d=map(int,input().split())
n=int(input())
a1=min(8*q,4*h,2*s,d)#2Lあたりの一番安い金額
a2=min(4*q,2*h,s)#1Lあたりの一番安い金額
if n%2==0:
    ans=(n//2)*a1
else:
    ans=(n//2)*a1+a2
print(ans)
