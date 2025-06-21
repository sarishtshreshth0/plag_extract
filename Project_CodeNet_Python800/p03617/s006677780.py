import sys
input = lambda: sys.stdin.readline().rstrip()
 
q,h,s,d=map(int,input().split())
n=int(input())

a=min(d,s*2,h*4,q*8) #2L
b=min(s,h*2,q*4) #1L
ans=0
ans+=(n//2)*a
n-=2*(n//2)
ans+=n*b
print(ans)