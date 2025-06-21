import sys

def solve():
    input = sys.stdin.readline
    Q, H, S, D = map(int, input().split())
    N = int(input())
    Double = [Q * 8, H * 4, S * 2, D]
    Single = [Q * 4, H * 2, S]
    if N % 2 == 0: print(min(Double) * N // 2)
    else: print(min(Double) * (N - 1) // 2 + min(Single))

    return 0

if __name__ == "__main__":
    solve()