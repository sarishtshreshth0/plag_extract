n = int(input())
a = list(map(int,input().split()))
r = [0 for _ in range(100001)]
for i in range(n):
    r[a[i]] += 1
ans = 0
for i in range(len(r)-2):
    ans = max(ans,sum(r[i:i+3]))
print(ans)