import sys

input = sys.stdin.readline


def main():
    N = int(input())
    C = [0] * (N - 1)
    S = [0] * (N - 1)
    F = [0] * (N - 1)
    for i in range(N - 1):
        C[i], S[i], F[i] = map(int, input().split())

    ans = [0] * N
    for i in range(N - 1):
        time = 0
        for c, s, f in zip(C[i:], S[i:], F[i:]):
            if time < s:
                time = s
            r = (time - s) % f
            time += f - r if r > 0 else 0
            time += c
        ans[i] = time

    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
