import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    S = input()

    stack = deque([])
    right = 0
    for i in range(N):
        if S[i] == "(":
            stack.append(S[i])
        else:
            if stack:
                stack.pop()
            else:
                right += 1

    ans = "(" * right + S + ")" * len(stack)
    print(ans)


if __name__ == "__main__":
    main()
