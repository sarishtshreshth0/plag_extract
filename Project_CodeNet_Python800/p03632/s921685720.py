import sys

input = sys.stdin.readline


def main():
    A, B, C, D = map(int, input().split())

    if B <= C or D <= A:
        ans = 0
    else:
        ans = min(B, D) - max(A, C)

    print(ans)


if __name__ == "__main__":
    main()
