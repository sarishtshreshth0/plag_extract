import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    W = list(map(int, input().split()))
    g = sum(W)
    ans = 10**6
    for i in range(1,N):
        t = abs(g-2*sum(W[:i]))
        ans = min(ans,t)

    print(ans)

if __name__ == "__main__":
    main()
