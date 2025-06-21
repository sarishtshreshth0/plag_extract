import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    a, b = nm()
    for c in range(1, 4):
        if a * b * c % 2 == 1:
            print('Yes')
            return
    print('No')


if __name__ == '__main__':
    main()
