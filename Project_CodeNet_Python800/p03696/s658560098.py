import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    N = int(input())
    S = str(input())
    stack_rem = 0

    need_left = 0

    for i in range(N):
        if S[i] == '(':
            stack_rem += 1
        elif stack_rem > 0:
            stack_rem -= 1
        else:
            need_left += 1
    need_right = stack_rem
    print('('*need_left+S+')'*need_right)

resolve()