import numpy as np
N,X = map(int,input().split())
Y = list(map(int,input().split()))
Z = [abs(y-X) for y in Y]
print(np.gcd.reduce(Z))