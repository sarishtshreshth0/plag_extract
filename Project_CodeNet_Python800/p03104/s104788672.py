a, b = map(int, input().split())

def odd(x):
    if ( (x + 1) // 2 ) % 2 == 0:
        return 0
    else:
        return 1

def solve(m):
    if m % 2 == 1:
        return odd(m)
    else:
        return odd(m + 1) ^ (m + 1)

print(solve(b) ^ solve(a - 1))