import math

N,K=map(int, input().split())

print(math.ceil(math.log(N,K)) if N!=1 else 1)