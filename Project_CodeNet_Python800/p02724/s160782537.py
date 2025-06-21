n = int(input())
ans = 0
if n//500>0:
    ans += 1000 * (n//500)
    n = n - 500 * (n//500)
if n//5>0:
    ans += 5 * (n//5)
print(ans)