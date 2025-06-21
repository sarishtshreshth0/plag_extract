def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))

from itertools import combinations
import math

def main():
    n, d = Input()
    x = [mapt(int, input().split()) for _ in range(n)]
    # print(x)
    comb = list(combinations(x,2))
    # print(comb)
    ans = 0
    for a, b in comb:
        r = 0
        for y, z in zip(a, b):

            r += abs(y-z)**2
            # print(y, z)
        r = math.sqrt(r)
        if (r*2)%2==0:
            ans += 1
    print(ans)

main()