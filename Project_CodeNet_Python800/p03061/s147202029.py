#create date: 2020-06-29 23:17

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    n = ni()
    a = na()
    l = [1] * n
    l[0] = a[0]
    r = [1] * n
    r[n-1] = a[n-1]
    for i in range(1, n):
        l[i] = gcd(l[i-1], a[i])
    for i in list(range(0, n-1))[::-1]:
        r[i] = gcd(r[i+1], a[i])
    ans = max(r[1], l[n-2])
    for i in range(1, n-1):
        ans = max(ans, gcd(l[i-1], r[i+1]))
    print(ans)

if __name__ == "__main__":
    main()