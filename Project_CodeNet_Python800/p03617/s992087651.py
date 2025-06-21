q, h, s, d = map(int, input().split())
n = int(input())

ans = n // 2 * min(q * 8, h * 4, s * 2, d)
if n % 2 == 1:
    ans += min(q * 4, h * 2, s)
print(ans)