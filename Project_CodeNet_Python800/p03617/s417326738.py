q,h,s,d = map(int,input().split())
n = int(input())

z = min(q*4,h*2,s)

if n % 2 != 0:
    print(min((n//2)*d+z,n*z))
else:
    print(min((n//2)*d,n*z))
