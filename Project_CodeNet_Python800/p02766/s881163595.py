import math
N,K=(map(int,input().split()))
digits = (math.floor(math.log(N)/math.log(K)) + 1)
print(digits)