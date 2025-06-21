import fractions

n,st=map(int,input().split())
*x,=map(int,input().split())

e=abs(x[0]-st)
for i in range(1,n):
    e=fractions.gcd(e,abs(x[i]-st))

print(e)