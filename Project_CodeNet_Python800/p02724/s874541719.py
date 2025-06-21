# B Golden Coins

X = int(input())

high, mod = divmod(X, 500)
low, mod = divmod(mod, 5)

ans = high * 1000 + low * 5
print(ans)