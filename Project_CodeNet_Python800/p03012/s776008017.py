n = int(input())
w = list(map(int,input().split()))
ans = 10**9
for i in range(1,n):
    l1 = w[:i]
    l2 = w[i:]
    ans = min(ans,abs(sum(l1)-sum(l2)))
print(ans)  