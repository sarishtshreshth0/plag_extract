
def resolve():
    MOD = 998244353
    N = int(input())
    D = list(map(int, input().split()))

    if D[0] != 0:
        print(0)
        return

    CNT = [0] * N
    for i in D:
        CNT[i] += 1

    if CNT[0] > 1:
        print(0)
        return

    ans = 1
    for i in range(1, N):
        ans *= pow(CNT[i - 1], CNT[i], MOD)
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    resolve()
