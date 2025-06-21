import sys
import math
import bisect

def main():
    a, b = map(int, input().split())
    if a == 1:
        a = 14
    if b == 1:
        b = 14
    if a > b:
        print('Alice')
    elif a < b:
        print('Bob')
    else:
        print('Draw')

if __name__ == "__main__":
    main()
