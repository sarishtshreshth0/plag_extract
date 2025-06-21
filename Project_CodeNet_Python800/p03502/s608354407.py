import sys
import math
import bisect

def query(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

def main():
    n = int(input())
    if n % query(n) == 0:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()
