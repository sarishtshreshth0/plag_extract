from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
d = defaultdict(int)

cum = 0
ans = 0
d[0] = 1
for i in a:
    cum += i
    ans += d[cum]
    d[cum] += 1
print(ans)
