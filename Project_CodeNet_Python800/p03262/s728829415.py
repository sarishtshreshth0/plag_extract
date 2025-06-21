import sys
read = sys.stdin.read
from math import gcd
from bisect import bisect
def main():
    n, x, *a = map(int, read().split())
    if n == 1:
        print(abs(a[0] - x))
        sys.exit()
    a.sort()
    a2 = [x - y for x, y in zip(a[1:], a)]
    xpos = bisect(a, x)
    if xpos == 0:
        xd = a[0] - x
        a2.append(xd)
        a2.append(xd)
    elif xpos == n:
        xd = x - a[-1]
        a2.append(xd)
        a2.append(xd)
    else:
        xd1 = x - a[xpos - 1]
        xd2 = a[xpos] - x
        a2.append(xd1)
        a2.append(xd2)
    if len(a2) == 2:
        r = gcd(a[0], a[1])
        print(r)
        sys.exit()

    r = gcd(a2[0], a2[1])
    for i1 in range(2, n + 1):
        r = gcd(r, a2[i1])
    print(r)

if __name__ == '__main__':
    main()
