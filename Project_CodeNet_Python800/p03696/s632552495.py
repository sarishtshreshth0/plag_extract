import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = input()

    insert_L = 0
    cnt_L = 0

    for s in S:
        if s == '(':
            cnt_L += 1
        else:
            if cnt_L:
                cnt_L -= 1
            else:
                insert_L += 1

    insert_R = cnt_L

    res = '(' * insert_L + S + ')' * insert_R
    print(res)


if __name__ == '__main__':
    resolve()
