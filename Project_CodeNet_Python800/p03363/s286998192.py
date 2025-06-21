from collections import defaultdict
n = int(input())
li_a = list(map(int, input().split()))
s = [0] * (n+1)
dd = defaultdict(lambda:0)
for i in range(n):
    s[i+1] += s[i] + li_a[i]
for i in range(n+1):
    dd[s[i]] += 1
ans = 0
for key in dd:
    ans += (dd[key]*dd[key] - dd[key])//2
print(ans)