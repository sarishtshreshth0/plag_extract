def odd_solve(n):
    return (n + 1) // 2 % 2

def solve(n):
    if n % 2 == 1:
        return odd_solve(n)
    else:
        return odd_solve(n + 1) ^ (n + 1)

a, b = map(int, input().split())
ans = solve(b) ^ solve(a - 1)
print(ans)
