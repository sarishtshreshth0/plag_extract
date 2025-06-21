import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from math import factorial
def C(n, m, P):
    c = 1
    for i in range(m):
        c *= n-i
        c %= P
    m = factorial(m)%P
    return c*pow(m, P-2, P)%P

def main():
    P = int(1e9)+7
    n, a, b = map(int, readline().split())
    print((pow(2, n, P)-1-C(n, a, P)-C(n, b, P))%P)
if __name__ == '__main__':
    main()
