import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from math import sqrt, ceil, log10
def main():
    n = int(input())
    sqrtn = ceil(sqrt(n))
    r = n
    for i1 in range(1, sqrtn + 1):
        if n % i1 == 0:
            t1 = log10(i1)
            t2 = log10(n//i1)
            t = max(t1, t2) + 1
            r = min(r, t)
    print(int(r))

if __name__ == '__main__':
    main()
