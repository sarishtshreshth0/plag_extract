import sys
input = sys.stdin.readline


def read():
    S = input().strip()
    return S,


def solve(S):
    N = len(S)
    ans = [0, 0]  # 偶数番目、奇数眼目の1の個数
    for i in range(N):
        if S[i] == "1":
            ans[i % 2] += 1
    return min(ans[0]+N//2-ans[1], N//2+N%2-ans[0]+ans[1])


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
