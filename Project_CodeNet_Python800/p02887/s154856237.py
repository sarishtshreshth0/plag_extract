import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    n = int(input())
    s = input().rstrip()
    ans = [s[0]]
    now = s[0]
    for i in s[1:]:
        if i != now:
            ans.append(i)
            now = i
    print(len(ans))

if __name__=="__main__":
    main()
