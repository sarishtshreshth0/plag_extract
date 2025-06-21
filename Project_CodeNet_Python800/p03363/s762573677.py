import sys
from itertools import accumulate
from collections import Counter


def main():
    n = sys.stdin.readline()
    print(sum([(n*(n-1))//2 for n in [n for n in Counter(list(accumulate([0]+list(map(int, sys.stdin.readline().rstrip().split()))))).values() if n > 1]]))

if __name__ == '__main__':
    main()