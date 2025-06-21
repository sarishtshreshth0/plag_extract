x = int(input())
ans, r = divmod(x, 500)
ans *= 1000
ans += (r//5)*5
print(ans)
