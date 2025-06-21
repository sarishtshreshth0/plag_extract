import math
x, b = list(map(lambda n: int(n), input().split(" ")))
print(math.floor(math.log(x, b)) + 1)