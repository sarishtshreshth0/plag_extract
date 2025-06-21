x = int(input())
q, r = divmod(x, 500)
ans = q*1000
ans += (r//5)*5
print(ans)
