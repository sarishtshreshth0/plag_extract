import math
N, K = map(int, input().split())
if N <= K:
    N = str(N)
    print(len(N))
else:
    print(math.ceil(math.log(N, K)))
