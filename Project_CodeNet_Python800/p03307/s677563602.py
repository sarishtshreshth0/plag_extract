a = 2
N = int(input())

#最大公約数
def gcd(a,N):
    while N!=0:
        a,N = N, a%N
    return a
##2つの整数a,bに対し，最大公約数g,最小公倍数lとおくと，
##ab=gl
print(int(a*N/gcd(a,N)))