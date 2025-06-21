import math

def input_li():
    return list(map(int, input().split()))


def input_int():
    return int(input())


N = input_int()
ans = len(str(N))
for i in range(1, math.ceil(N ** 0.5) + 1):
    if (N / i).is_integer():
        ans = min(ans, max(len(str(i)), len(str(N // i))))
print(ans)
