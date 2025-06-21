import sys

input = sys.stdin.readline

P = 998244353


def main():
    N = int(input())
    D = list(map(int, input().split()))

    cnt = [0] * (max(D) + 1)
    for d in D:
        cnt[d] += 1

    if not ((D[0] == 0) and (cnt[0] == 1) and (0 not in cnt)):
        print(0)
    else:
        ans = 1
        for i in range(len(cnt) - 1):
            ans *= pow(cnt[i], cnt[i + 1], P)  # a**b mod p
            ans %= P
        print(ans)


if __name__ == "__main__":
    main()
