import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def main():
    N = int(input())
    reds = []
    for _ in range(N):
        a, b = map(int, input().split())
        reds.append((a, b))

    blues = []
    for _ in range(N):
        c, d = map(int, input().split())
        blues.append((c, d))

    reds.sort(key=lambda x: x[0])
    blues.sort(key=lambda x: x[0])
    used = [False] * N

    ans = 0
    for i in range(N):
        b = blues[i]
        max_r = -1
        max_j = None
        for j in range(N):
            r = reds[j]
            if b[0] < r[0]:
                continue
            if b[1] < r[1]:
                continue

            if not used[j] and max_r < r[1]:
                max_r = r[1]
                max_j = j

        if max_j is not None:
            used[max_j] = True
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
