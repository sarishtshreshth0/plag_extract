n,k = map(int,input().split())

ans = 0
while n >= k:
    ans += 1
    n = n//k

print(ans+1)