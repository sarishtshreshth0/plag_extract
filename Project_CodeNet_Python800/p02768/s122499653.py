N, A, B = [int(_) for _ in input().split()]
mod = 10**9 + 7
c = [1, N]
for i in range(1, B + 1):
    c += [c[-1] * (N - i) * pow(i + 1, mod - 2, mod) % mod]
ans = pow(2, N, mod) - c[A] - c[B] - 1
ans %= mod
print(ans)
