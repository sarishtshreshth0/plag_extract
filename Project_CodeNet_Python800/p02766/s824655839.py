N ,K = (int(a) for a in input().split())
ans = 0
while N > 0 :
    N = N // K
    ans += 1
print(ans)