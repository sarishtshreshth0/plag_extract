import sys


read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
s_readline = sys.stdin.readline

S = list(map(int, s_readline().rstrip()))
N = len(S)


def solve():

    ans = 0
    for i in range(N - 1):
        if S[i + 1] == S[i]:
            S[i + 1] = not S[i + 1]
            ans += 1

    print(ans)


if __name__ == '__main__':
    solve()
