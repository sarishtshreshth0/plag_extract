import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9

def main():
    n = int(input())

    S = list(str(n))
    h = 0
    for s in S:
        h += int(s)
    if n%h == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
