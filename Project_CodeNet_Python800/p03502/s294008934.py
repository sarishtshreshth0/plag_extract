import sys

input = sys.stdin.readline


def main():
    N = int(input())

    f = sum(int(d) for d in str(N))
    if N % f == 0:
        ans = "Yes"
    else:
        ans = "No"

    print(ans)


if __name__ == "__main__":
    main()
