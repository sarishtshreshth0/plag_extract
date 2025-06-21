import sys
from math import gcd

input = sys.stdin.readline


def lcm(a, b):
    return (a * b) // gcd(a, b)


def main():
    N = int(input())

    ans = lcm(2, N)

    print(ans)


if __name__ == "__main__":
    main()
