import sys
import copy
import math
import bisect
import pprint
import bisect
from functools import reduce
from copy import deepcopy
from collections import deque

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

if __name__ == '__main__':
    a = [int(i) for i in input().split()]

    if (a[0] < a[1] and a[0]<a[2] and a[2] <a[1]) or (a[0] > a[1] and a[0]>a[2] and a[2] >a[1]):
        print("Yes")
    else:
        print("No")
