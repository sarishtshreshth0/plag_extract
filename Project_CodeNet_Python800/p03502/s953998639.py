import sys
import numpy as np
import math  # gcdもあるよ
from collections import deque
from collections import defaultdict
from copy import deepcopy
from itertools import accumulate #リストを与えると累積和を返す
def input(): return sys.stdin.readline().rstrip()
from functools import lru_cache #メモ化

def main():
    n = int(input())
    a = list(str(n))
    A = [int(a[i]) for i in range(len(a))]
    A = sum(A)
    if n % A == 0:
        print('Yes')
    else: print('No')
    
    return 0

if __name__ == "__main__":
    main()