import math
N,X  = (int(T) for T in input().split())
Cor  = sorted([abs(int(T)-X) for T in input().split()])
GCDC = Cor[0]
for T in range(1,N):
    GCDC = math.gcd(GCDC,Cor[T])
    if GCDC==1: break
print(GCDC)