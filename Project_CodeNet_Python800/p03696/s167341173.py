import math
import collections
import fractions
import itertools
import functools
import  operator

def solve():
    n = int(input())
    s = input()
    l, r = 0, 0
    for i in s:
        if i == "(":
            r += 1
        else:
            if r != 0:
                r -= 1
            else:
                l += 1
    ans = "("*l + s + ")"*r
    print(ans)
    return 0

if __name__ == "__main__":
    solve()
