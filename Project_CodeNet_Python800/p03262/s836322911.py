import functools
import math

N, X = [int(i) for i in input().split()]
x_list = [int(i) for i in input().split()]

x_list.append(X)
num_list = sorted(x_list)
 
tmp = map(lambda x: abs(x[0] - x[1]),
          zip(num_list[:-1],num_list[1:]))

D = functools.reduce(lambda acc, x: math.gcd(acc, x), tmp, 0)

print(D)
