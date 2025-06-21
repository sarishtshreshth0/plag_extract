#create date: 2020-06-30 15:26

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    a, b = na()
    if b - a < 5:
        ans = 0
        for x in range(a, b+1):
            ans ^= x
        print(ans)
        quit()
    left, right = 0, 0
    if a % 4 == 0:
        left = 0
    else:
        for i in range(a % 4, 4):
            x = (a // 4) * 4 + i
            left ^= x
    if b % 4 == 0:
        right = b
    else:
        for i in range(0, b % 4+1):
            y = (b // 4) * 4 + i
            right ^= y
    print(left^right)

if __name__ == "__main__":
    main()