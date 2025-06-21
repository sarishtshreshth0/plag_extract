from decimal import Decimal

Q, H, S, D = map(int, input().split())
N = int(input())

# 1リットルあたりの単価を出す
s = min([Q*4, H*2, S])
d = Decimal(D)/2

# Nが2で割れる時はリッターあたりの最安値*N
if N%2==0:
    print(int(N*min(s, d)))

# Nが2で割れない時は、N-1までは最安値で買って、残り1リットルはsの単価で買う
else:
    print(int((N-1)*min(s, d) + s))