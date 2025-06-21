import sys
import math

input = sys.stdin.readline


def main():
    n = int(input())
    print(n if n % 2 == 0 else n * 2)


if __name__ == "__main__":
    main()
