ans=0
q,h,s,d=map(int,input().split())
n=int(input())
l=[(q,q*8,0.25),(h,h*4,0.5),(s,s*2,1),(d,d,2)]
l.sort(key=lambda x:-x[1])
while n>0:
    c=l.pop()
    ans+=c[0]*int(n//c[2])
    n-=c[2]*int(n//c[2])
    
print(ans)
