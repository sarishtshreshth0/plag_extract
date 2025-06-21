n,k = map(int,input().split())
for i in range(10**5):
    if n == 1:
        ans = 1
    elif k**(i-1) <= n < k**i:
        continue
    elif k**(i-1) > n:
        ans = i-1
        break
print(ans)