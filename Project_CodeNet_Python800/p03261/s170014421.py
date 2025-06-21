import sys
import heapq
import math


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())

    l = "A"
    s = set()

    for i in range(N):

        w = input()
        if w[0] != l and i!=0:
            print("No")
            exit()
        if w in s:
            print("No")
            exit()
        l = w[-1]
        s.add(w)

    print("Yes")


if __name__ == "__main__":
    main()
