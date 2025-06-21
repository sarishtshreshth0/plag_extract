N = int(input())
l = list(map(int, input().split()))

ans = 999999

for i in range(N):
    f = l[:i]
    s = l[i:]
    diff = abs(sum(f)-sum(s))
    if diff <= ans:
        ans = diff
    
print(ans)