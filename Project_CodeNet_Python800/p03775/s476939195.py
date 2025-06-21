# from pprint import pprint
import math

# import collections

n = int(input())


# n, k = map(int, input().split(' '))
# a = list(map(int, input().split(' ')))


def f(a, b):
    return max(math.floor(math.log10(a)+1), math.floor(math.log10(b))+1)


a = 1
ans = 11
while a <= math.sqrt(n):
    if n % a == 0 and f(a, n // a) <= ans:
        ans = f(a, n // a)
    a += 1

print(ans)
