X = int(input())
ans = 0
div, mod = divmod(X, 500)
ans += div*1000
div, mod = divmod(mod, 5)
ans += div*5
print(ans)