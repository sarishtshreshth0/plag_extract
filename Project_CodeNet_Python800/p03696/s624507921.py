import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    N = int(input())
    S = str(input())
    left_over = 0
    right_over = 0

    for i in range(N):
        if S[i] == '(':
            left_over += 1
        else:
            left_over -= 1
            if left_over < 0:
                right_over = max(right_over, -left_over)

    SS = '('*right_over+S

    left_over = 0
    for i in range(len(SS)):
        if SS[i] == '(':
            left_over += 1
        else:
            left_over -= 1

    print(SS+')'*left_over)


resolve()