import sys
read = sys.stdin.read
from math import gcd
def main():
    n, *a = map(int, read().split())
    if n == 1:
        print(a[0])
        sys.exit()
    l = [0] * (n + 1)
    for i1 in range(n):
        l[i1 + 1] = gcd(l[i1], a[i1])
    r = [0] * (n + 1)
    for j1 in range(n - 1, -1, -1):
        r[j1] = gcd(r[j1 + 1], a[j1])
    m = [0] * (n + 1)
    for k1 in range(n):
        m[k1] = gcd(l[k1], r[k1 + 1])
    r = max(m)
    print(r)

if __name__ == '__main__':
    main()