import math
import collections
import itertools
import heapq
import sys

def main():
    X = int(input())

    res = (X // 500)*1000 + (((X % 500))//5)*5

    print(res)


if __name__ == "__main__":
    main()