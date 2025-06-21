import sys
from collections import defaultdict

input = sys.stdin.readline
P = 998244353


def main():
    N = int(input())
    D = list(map(int, input().split()))

    count = defaultdict(int)
    for d in D:
        count[d] += 1

    if not(D[0] == 0 and count[0] == 1):
        print(0)
        exit()

    max_depth = max(count.keys())
    ans = 1
    for d in range(max_depth):
        ans = (ans * pow(count[d], count[d + 1], mod=P)) % P

    print(ans)


if __name__ == "__main__":
    main()
