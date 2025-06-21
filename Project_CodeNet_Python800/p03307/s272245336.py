from fractions import gcd

n=int(input())
g=gcd(2,n)
print(2*n//g)