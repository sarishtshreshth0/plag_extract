a,b,c,d= map(int,input().split())
A=min(min(4*a,2*b),c)
B=min(2*A,d)

n=int(input())
if n %2==0:
    print(n*B//2)
else:
    print((n//2)*B + A)