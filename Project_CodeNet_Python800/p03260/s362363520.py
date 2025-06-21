import sys
import math
import bisect

def main():
    a, b = map(int, (input().split()))
    ans = False
    for i in range(1, 4):
        if a * b * i % 2 == 1:
            ans = True
    if ans:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()
