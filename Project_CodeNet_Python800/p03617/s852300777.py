q,h,s,d=map(int, input().split( ))
n=int(input())#ちょうど
n*=4
lst=[(q*4,q,1),(h*2,h,2),(s,s,4),(d/2,d,8)]
lst.sort()
ans=0
for _,t,x in lst:
    ans+=(n//x)*t
    n-=(n//x)*x
print(ans)
