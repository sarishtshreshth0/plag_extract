import sys
import math
from functools import reduce


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


def main():
    n, x = nm()
    X = nl()
    X.append(x)
    X = sorted(X)
    D = [X[i + 1] - X[i] for i in range(len(X) - 1)]
    ans = gcd_list(D)
    print(ans)


if __name__ == '__main__':
    main()
