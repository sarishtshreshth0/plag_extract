import math
n,k = map(int, input().split())
if n != 1:
    print(math.ceil(math.log(n,k)))
else:
    print(1)