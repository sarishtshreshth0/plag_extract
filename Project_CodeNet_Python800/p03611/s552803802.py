N = int(input())

a = list(map(int,input().split()))

memo = [0]*(2+10**5)

for i in range(N):
    tmp = a[i]
    memo[tmp-1] += 1
    memo[tmp] += 1
    memo[tmp+1] += 1

ans = max(memo)

print(ans)