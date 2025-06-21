def f(x):
    if x < 10:
        return x
    else:
        return x % 10 + f(x // 10)


n = int(input())
ans = "Yes" if n % f(n) == 0 else "No"
print(ans)
