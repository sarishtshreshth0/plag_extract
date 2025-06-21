n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

import fractions
#gcd=fractions.gcd(2,n)#最大公約数
lcm=(2//fractions.gcd(2,n))*n #最小公倍数

print(lcm)


