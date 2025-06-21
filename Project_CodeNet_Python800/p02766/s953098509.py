import math
N ,K = map(int,input().split())
a = math.log(N,K)
print(math.floor(a+1))
