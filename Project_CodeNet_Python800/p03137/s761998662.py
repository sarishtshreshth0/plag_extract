import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n, m = nm()
    X = nl()
    if n >= m:
        print(0)
    else:
        X = sorted(X)
        D = [X[i + 1] - X[i] for i in range(m - 1)]
        D = sorted(D, reverse=True)
        print(sum(D[n - 1:]))


if __name__ == '__main__':
    main()
