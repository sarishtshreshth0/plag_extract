import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    words = []
    flag = True
    for i in range(n):
        w = ns()
        if w in words:
            flag = False
        elif i != 0 and w[0] != words[-1][-1]:
            flag = False
        else:
            words.append(w)
    print('Yes' if flag else 'No')


if __name__ == '__main__':
    main()
