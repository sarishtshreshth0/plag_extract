import numpy as np
import math
import collections
import fractions
import itertools

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ruiseki = [0]
    ans = 0
    for i in range(n):
        ruiseki.append(ruiseki[i]+a[i])
    c = collections.Counter(ruiseki).values()
    for i in c:
        ans += i*(i-1)//2
    print(ans)
    return 0

if __name__ == "__main__":
    solve()
#fooooooooooooooo!! yattaze!! AC!!