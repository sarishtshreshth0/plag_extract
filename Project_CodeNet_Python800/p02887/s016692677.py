import sys

# import bisect
# import numpy as np
# from collections import deque
from collections import deque
# map(int, sys.stdin.read().split())
# import heapq
import bisect
import math

def input():
    return sys.stdin.readline().rstrip()


def main():
    N =int(input())
    S = input()
    pre ="A"
    count=0
    for i in S:
        if i !=pre:
            count+=1
        pre = i
    print(count)


if __name__ == "__main__":
    main()
