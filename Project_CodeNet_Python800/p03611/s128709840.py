N = int(input())
a = [int(x) for x in input().split()]
memo = [0]*(10**5+2)
ans = 1
for i in range(N):
  memo[a[i]] += 1
  memo[a[i]+1] += 1
  memo[a[i]-1] += 1
print(max(memo))
