import math
from functools import reduce


def gcd_list(l):
    return reduce(math.gcd, l)


def solve():
    N, X = map(int, input().split())
    x = map(int, input().split())
    xX = [abs(X - i) for i in x]
    print(gcd_list(xX))


if __name__ == '__main__':
    solve()
