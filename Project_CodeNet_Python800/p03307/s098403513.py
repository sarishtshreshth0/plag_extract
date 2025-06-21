
N = int(input())

import fractions
#a,b=13*7*8, 52*9*11
f=fractions.gcd(2,N)
f2=2*N//f
print(f2)