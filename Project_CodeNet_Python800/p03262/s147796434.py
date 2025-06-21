import math

def agcd(l):
    a=math.gcd(l[0],l[1])
    for i in range(2,len(l)):
        a=math.gcd(a,l[i])
    return a

N,X=map(int,input().split())
x=[abs(i-X) for i in list(map(int,input().split()))]

print(agcd(x)if 1<N else x[0])