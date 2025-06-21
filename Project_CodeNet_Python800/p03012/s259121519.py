#create date: 2020-07-25 09:13

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n = ni()
    w = na()
    l, r = 0, sum(w)
    ans = 10**10
    for i in range(0, n-1):
        l += w[i]
        r -= w[i]
        ans = min(ans, abs(l - r))
    print(ans)

if __name__ == "__main__":
    main()