a,b,c,d=map(int,input().split())
n=int(input())

twoval=min(8*a,4*a+2*b,4*b,2*b+c,2*c,d)
oneval=min(4*a,2*b,2*a+b,c)

if n%2==0:
    print(twoval*(n//2))
else:
    print(oneval+twoval*((n-1)//2))
    
