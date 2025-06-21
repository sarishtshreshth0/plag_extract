a,b,c,d=map(int, input().split())
n=int(input())
oneltr=min(4*a, 2*b, c, 2*a+b)
twoltr=min(8*a, 4*b, 2*c, d, c+2*b, c+b+2*a,c+4*a,4*a+2*b,b+6*a,3*b+2*a)

if n%2==0 :
               print(twoltr * (n//2))
else :
               print(oneltr+twoltr * ((n-1)//2))
