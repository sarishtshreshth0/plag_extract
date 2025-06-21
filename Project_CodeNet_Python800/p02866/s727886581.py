def powmod(n: int, p: int, M: int) -> int:
    ans = 1
    for _ in range(p):
        ans *= n
        ans %= M
    return ans

def solve():
    N = int(input())

    distances = list(map(int, input().split()))

    node = [0] * N

    for distance in distances:
        node[distance] += 1

    ans = 1
    MOD = 998244353

    if distances[0] != 0 or node[0] != 1:
        print(0)
    else:
        previous = node[1]
        for i in range(2,N):
            now = node[i]
            ans = ans * powmod(previous, now, MOD) % MOD
            previous = now
        print(ans)
    
solve()