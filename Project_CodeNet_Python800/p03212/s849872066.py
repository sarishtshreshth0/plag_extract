import sys
sys.setrecursionlimit(10 ** 7)

def solve(p, n, bt):
    if n < p:
        return 0
    pre = bt
    tmp = 0
    for i, v in enumerate([7, 5, 3]):
        q = 10*p + v
        bt |= 1<<i
        if q <= n and bt == 7:
            tmp += 1
        tmp += solve(q, n, bt)
        bt = pre
    return tmp

def main():
    n = int(input())
    print(solve(0, n, 0))

if __name__ == "__main__":
    main()