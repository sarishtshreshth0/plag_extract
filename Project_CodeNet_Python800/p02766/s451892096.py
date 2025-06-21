n,k = map(int,input().split())
ans = 1
while n >= k:
    ans += 1
    n //= k
print(ans)