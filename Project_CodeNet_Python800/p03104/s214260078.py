# 0123の周期でXORはリセットされるため剰余だけ考える
def solve(x):
    if x % 4 == 3:
        return 0
    elif x % 4 == 0:
        return x
    elif x % 4 == 1:
        return x ^ (x - 1)
    elif x % 4 == 2:
        return x ^ (x - 1) ^ (x - 2)


a, b = map(int, input().split())


print(solve(a - 1) ^ solve(b))