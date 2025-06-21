import sys

input = sys.stdin.readline


def main():
    A, B, C = map(int, input().split())

    if A < B:
        if A < C < B:
            ans = "Yes"
        else:
            ans = "No"
    else:
        if B < C < A:
            ans = "Yes"
        else:
            ans = "No"

    print(ans)


if __name__ == "__main__":
    main()
