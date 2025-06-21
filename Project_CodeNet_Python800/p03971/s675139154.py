import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, A, B = map(int, readline().split())
    S = input()
    cnt_a = 0
    cnt_b = 0

    for char in S:
        flag = False
        if char == "a":
            if cnt_a + cnt_b < A + B:
                cnt_a += 1
                flag = True
        elif char == "b":
            if cnt_a + cnt_b < A + B:
                if cnt_b < B:
                    cnt_b += 1
                    flag = True
        print("Yes" if flag else "No")


if __name__ == '__main__':
    main()
